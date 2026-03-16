import os
from fastapi import FastAPI
from smart_agri_agent import root_agent
import uvicorn

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "healthy"}  # REQUIRED for Cloud Run

@app.get("/")
async def home():
    return {"message": "Smart Agriculture Agent running"}

@app.post("/ask")  # Changed to POST for better agent handling
async def ask_endpoint(query: dict):
    from google.adk.runners import Runner
    runner = Runner()
    response = await runner.run(root_agent, query.get("q", ""))
    return {"response": response.content if response else "No response"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
