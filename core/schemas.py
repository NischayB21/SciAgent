from pydantic import BaseModel
from typing import List, Optional, Dict, Any


# -----------------------------
# Search Request
# -----------------------------
class SearchRequest(BaseModel):
    topic: str
    author: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


# -----------------------------
# Paper Model
# -----------------------------
class Paper(BaseModel):
    title: str
    authors: List[str]
    summary: str
    published: str
    pdf_url: str
    source: str


# -----------------------------
# Paper Analysis
# -----------------------------
class PaperAnalysis(BaseModel):
    title: str
    summary: str
    methods: List[str]
    datasets: List[str]
    limitations: List[str]


# -----------------------------
# Knowledge Result
# -----------------------------
class KnowledgeResult(BaseModel):
    status: str
    paper: str
    embedding_dimension: int
    methods: List[str]
    datasets: List[str]


# -----------------------------
# Search Response
# -----------------------------
class SearchResponse(BaseModel):
    topic: str
    papers: List[Paper]
    analyses: List[PaperAnalysis]
    knowledge: List[KnowledgeResult]
    gap_report: Dict[str, Any]
    recommendations: List[Dict[str, Any]]