# Rapport de Test de l'API - Student Learning Assistant

## 1. Introduction
Ce rapport documente les tests manuels et automatisés réalisés sur l'API FastAPI afin de valider la robustesse des modèles Pydantic, la structure des réponses JSON et le bon fonctionnement des routeurs.

## 2. Endpoints Testés
- **`GET /health`** : Vérifie l'état de santé de l'API et retourne un horodatage UTC.
- **`POST /chat`** : Gère les messages de l'assistant.
- **`POST /quiz/`** : Génère un quiz structuré basé sur un sujet, un nombre de questions et d'options.
- **`POST /summarize/`** : Fournit un résumé structuré en puces.

## 3. Résultats des Tests Manuels (Swagger UI)
- **Requête valide (`POST /quiz/`)** :
  - *Payload* : `{"subject": "Python", "number_quizzes": 3, "number_options": 4}`
  - *Statut attendu* : `200 OK`
  - *Résultat* : Succès, retour d'un objet JSON contenant la liste détaillée des questions, options et réponses correctes.
- **Requête invalide (`POST /quiz/`)** :
  - *Payload* : `{"subject": "Python", "number_quizzes": 15, "number_options": 4}` *(dépasse la limite max de 10)*
  - *Statut attendu* : `422 Unprocessable Entity`
  - *Résultat* : Succès, rejet automatique par la validation Pydantic.

## 4. Tests Automatisés (`pytest`)
Tous les tests automatisés écrits dans `tests/test_api.py` ont été exécutés avec succès :
- `test_health_check` -> **PASSED**
- `test_post_quiz_valid` -> **PASSED**
- `test_post_quiz_invalid` -> **PASSED**