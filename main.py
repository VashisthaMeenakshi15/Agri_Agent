import os
import asyncio
from fastapi import FastAPI
from smart_agri_agent import root_agent
import uvicorn
from google.adk.runners import Runner

app = FastAPI()
runner = Runner()

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/")
async def home():
    return {"message": "Smart Agriculture Agent running"}

@app.get("/ask")
async def ask(q: str):
    try:
        # Run agent ASYNC - timeout after 30s
        loop = asyncio.get_event_loop()
        response = await asyncio.wait_for(
            loop.run_in_executor(None, lambda: runner.run_sync(root_agent, q)),
            timeout=30.0
        )
        return {"response": response.content if response else "No response"}
    except asyncio.TimeoutError:
        return {"error": "Agent timeout - try simpler query"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
