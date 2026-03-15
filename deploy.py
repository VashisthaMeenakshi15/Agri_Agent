import vertexai
from vertexai.preview import agent_engines

# import the agent created in agent.py
from agent import root_agent

# Initialize Vertex AI
vertexai.init(
    project="fytzibz-ccai-gcp-sandbox",  
    location="us-central1"
)


# Deploy agent to Vertex AI Agent Engine
agent_engines.create(
    display_name="smart-agri-agent",
    agent=root_agent
)

print("Agent deployment started successfully.")
