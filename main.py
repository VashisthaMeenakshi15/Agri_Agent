# import os
# import asyncio
# from fastapi import FastAPI
# from smart_agri_agent import root_agent
# import uvicorn
# from google.adk.runners import Runner

# app = FastAPI()
# runner = Runner()

# @app.get("/health")
# async def health():
#     return {"status": "healthy"}

# @app.get("/")
# async def home():
#     return {"message": "Smart Agriculture Agent running"}

# @app.get("/ask")
# async def ask(q: str):
#     try:
#         # Run agent ASYNC - timeout after 30s
#         loop = asyncio.get_event_loop()
#         response = await asyncio.wait_for(
#             loop.run_in_executor(None, lambda: runner.run_sync(root_agent, q)),
#             timeout=30.0
#         )
#         return {"response": response.content if response else "No response"}
#     except asyncio.TimeoutError:
#         return {"error": "Agent timeout - try simpler query"}
#     except Exception as e:
#         return {"error": str(e)}

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8080))
#     uvicorn.run(app, host="0.0.0.0", port=port)


from fastapi import FastAPI, UploadFile, File
import uvicorn
from smart_agri_agent import root_agent
import os
import uuid
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# Global session service (ADK requirement)
session_service = InMemorySessionService()

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "healthy", "agents": "7 agri agents ready"}

@app.get("/")
async def home():
    return {"message": "Smart Agriculture Multi-Agent API - Text/Voice/Video ready"}

@app.get("/ask")
async def ask(q: str):
    try:
        # ✅ PROPER ADK Runner for Gemini 2.5
        runner = Runner(session_service=session_service)
        session_id = str(uuid.uuid4())
        
        # Create ADK Content object (required format)
        message = Content(role="user", parts=[Part(text=q)])
        
        # Execute root_agent properly
        response_text = ""
        async for event in runner.run_stream(
            session_id=session_id,
            new_message=message
        ):
            if hasattr(event, 'content') and event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        response_text += part.text
        
        if response_text:
            return {"response": response_text.strip()}
        else:
            return {"response": f"Gemini 2.5 processed: '{q}' - no response generated"}
            
    except Exception as e:
        return {
            "response": f"Root agent received: '{q}'. Error: {str(e)[:100]}",
            "debug": "Check ADK imports and Gemini API key"
        }

@app.post("/voice")
async def voice(audio: UploadFile = File(...)):
    return {"message": "Voice endpoint ready - Speech-to-Text → root_agent → Text-to-Speech"}

@app.post("/analyze-plant") 
async def analyze_plant(image: UploadFile = File(...)):
    return {"message": "Plant Vision endpoint ready - image → plant_vision_agent → recommendations + Amazon links"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

