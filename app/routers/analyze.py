from fastapi import APIRouter
from app.models.schemas import AnalyzeRequest
from app.services.llm_agent import analyze_text

router = APIRouter(prefix="/analyze", tags=["Analyze"])

@router.post("/")
def analyze(req: AnalyzeRequest):
    return {"analysis": analyze_text(req.text, req.provider, req.model)}