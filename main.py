from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    # Update this to match your new return statement:
    assert response.json()["status"] == "Active"
    assert "environment" in response.json()
