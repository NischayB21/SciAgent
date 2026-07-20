from fastapi import APIRouter

from core.schemas import SearchRequest
from agents.supervisor.supervisor import supervisor

router = APIRouter()


@router.post("/search")
def search(request: SearchRequest):

    return supervisor.run(
        topic=request.topic,
        author=request.author,
        start_date=request.start_date,
        end_date=request.end_date
    )