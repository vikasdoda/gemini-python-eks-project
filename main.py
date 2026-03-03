from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Active", "environment": os.getenv("ENV", "Development")}

@app.get("/health")
def health_check():
    # This is crucial for Kubernetes later
    return {"status": "healthy"}
