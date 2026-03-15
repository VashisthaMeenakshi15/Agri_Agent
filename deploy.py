import vertexai
from vertexai.preview import agent_engines
from agents.root_agent import root_agent

vertexai.init(
    project="fytzibz-ccai-gcp-sandbox",
    location="us-central1"
)

agent_engines.create(
    display_name="agri-agent",
    agent=root_agent
)
