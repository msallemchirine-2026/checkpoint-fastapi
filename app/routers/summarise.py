from fastapi import APIRouter, HTTPException
from app.models import SummarizeRequest, SummarizeResponse

router = APIRouter(
    prefix="/summarize",
    tags=["summarize"]
)

@router.post("/", response_model=SummarizeResponse)
def summarize_text(request: SummarizeRequest):
    clean_text = request.text.strip()
    
    if not clean_text:
        raise HTTPException(
            status_code=400,
            detail="Le texte à résumer ne peut pas être vide."
        )
    
    nb_bullets = min(request.max_bullets, 5)
    simulated_summary = [
        f"Point clé {i} du texte fourni."
        for i in range(1, nb_bullets + 1)
    ]
    

    word_count = len(clean_text.split())
    
    return SummarizeResponse(
        summary=simulated_summary,
        word_count=word_count
    )