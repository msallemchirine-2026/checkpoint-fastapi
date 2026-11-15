from fastapi import APIRouter ,HTTPException
from app.models import ChatRequest, ChatResponse
router = APIRouter(prefix="/chat",
                   tags = ["chat"])
@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    clean_msg = request.message.strip()
    
    if not clean_msg:
        raise HTTPException(
            status_code=400,
            detail="Message can not be empty"
        )
    answer = f"J'ai bien reçu : {clean_msg}"
    
    return ChatResponse(
        answer="answer",
        model="model",
        tokens_used=len(clean_msg.split())
    )