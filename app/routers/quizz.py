from fastapi import APIRouter
from app.models import QuizzRequest, QuizzResponse, Quizz

router = APIRouter(
    prefix="/quiz",
    tags=["quiz"]
)

@router.post("/", response_model=QuizzResponse)
def generate_quiz(request: QuizzRequest):
    quizz_list = []

    for i in range(1, request.number_quizzes + 1):
        options_list = [f"Option A", f"Option B", f"Option C"]
        if request.number_options >= 4:
            options_list.append(f"Option D")

        quizz_list.append(
            Quizz(
                question=f"Question {i} sur le sujet : {request.subject} ?",
                options=options_list[:request.number_options],
                correct=options_list[0]
            )
        )

    return QuizzResponse(
        topic=request.subject,
        nb_questions=len(quizz_list),
        quizz=quizz_list
    )