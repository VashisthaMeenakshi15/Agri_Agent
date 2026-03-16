from fastapi import FastAPI
from smart_agri_agent import root_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Agriculture Agent running"}

@app.get("/ask")
def ask(q: str):
    response = root_agent.run(q)
    return {"response": response}
