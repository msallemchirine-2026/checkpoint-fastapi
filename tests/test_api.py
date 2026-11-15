from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Test de la route GET /health"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["message"] == "API IS RUNNING"

def test_post_quiz_valid():
    """Test de la route POST /quiz/ avec des données valides"""
    payload = {
        "subject": "Python",
        "number_quizzes": 2,
        "number_options": 4
    }
    response = client.post("/quiz/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["topic"] == "Python"
    assert data["nb_questions"] == 2
    assert len(data["quizz"]) == 2

def test_post_quiz_invalid():
    """Test de la route POST /quiz/ avec un nombre de questions invalide (hors limites)"""
    payload = {
        "subject": "Python",
        "number_quizzes": 15,  # Dépasse la limite max (le=10)
        "number_options": 4
    }
    response = client.post("/quiz/", json=payload)
    # Pydantic doit rejeter la requête avec une erreur 422
    assert response.status_code == 422