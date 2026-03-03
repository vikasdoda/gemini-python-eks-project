from fastapi.testclient import TestClient
from app.main import app # Import your FastAPI app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"} # Adjust this to match your actual code
