from fastapi import FastAPI
from pydantic import BaseModel

from core.schemas import Paper

from agents.search_agent.search_agent import search_agent
from agents.download_agent.download_agent import download_agent

from agents.analysis_agent.analysis_agent import analysis_agent
from agents.knowledge_agent.knowledge_agent import knowledge_agent
from agents.gap_agent.gap_agent import gap_agent
from agents.recommendation_agent.recommendation_agent import recommendation_agent

app = FastAPI(
    title="SciAgent API",
    version="2.0"
)


# -------------------------------------------------
# Request Models
# -------------------------------------------------

class ResearchRequest(BaseModel):
    topic: str


class AnalyzeRequest(BaseModel):
    paper: Paper


# -------------------------------------------------
# Root
# -------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "SciAgent Backend Running"
    }


# -------------------------------------------------
# Search Papers
# -------------------------------------------------

@app.post("/research")
def research(request: ResearchRequest):

    papers = search_agent.search(
        topic=request.topic
    )

    return {
        "count": len(papers),
        "papers": papers
    }


# -------------------------------------------------
# Analyze Paper
# -------------------------------------------------

@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    paper = request.paper

    # -----------------------------------------
    # PDF AVAILABLE -> Full RAG Pipeline
    # -----------------------------------------
    if paper.pdf_url:

        pdf_path = download_agent.download(paper)

        analysis = analysis_agent.analyze(
            title=paper.title,
            pdf_path=pdf_path
        )

    # -----------------------------------------
    # NO PDF -> Abstract Analysis
    # -----------------------------------------
    else:

        analysis = analysis_agent.analyze_text(
            title=paper.title,
            text=paper.summary
        )

    # -----------------------------------------
    # Remaining Agents
    # -----------------------------------------
    knowledge = knowledge_agent.process(analysis)

    gaps = gap_agent.analyze(analysis)

    recommendations = recommendation_agent.recommend(
        analysis,
        gaps
    )

    return {
        "paper": paper,
        "analysis": analysis,
        "knowledge": knowledge,
        "gaps": gaps,
        "recommendations": recommendations
    }