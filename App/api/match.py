from fastapi import APIRouter
from App.services.embeddings import store_resume_embedding
from App.services.matcher import match_resume
from App.models.match_request import MatchRequest
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/match", tags=["Matching"])

@router.post("/")
def match(request: MatchRequest):
    try:
        vector_db = store_resume_embedding(
            request.resume,
            persist_dir=r"C:\Users\gadda\OneDrive\Desktop\AI_Resume_Parser\Vector_store\Chroma"
        )
        return match_resume(vector_db, request.job_description)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
