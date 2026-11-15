from fastapi import FastAPI
from datetime import datetime, timezone
from app.routers import chat  
from app.routers import quizz
from app.routers import summarise
app = FastAPI(
    title="Student Learning Assistant API",
    version="1.0.0"
)

app.include_router(chat.router)
app.include_router(quizz.router)
app.include_router(summarise.router)




@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "API IS RUNNING",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": "1.0.0"
    }