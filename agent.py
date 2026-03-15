from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool
from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.tools import url_context

crop_knowledge_agent_google_search_agent = LlmAgent(
  name='Crop_Knowledge_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
crop_knowledge_agent_url_context_agent = LlmAgent(
  name='Crop_Knowledge_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
crop_knowledge_agent = LlmAgent(
  name='crop_knowledge_agent',
  model='gemini-2.5-flash',
  description=(
      'An agricultural knowledge agent that answers farmer questions related to crops, fertilizers, soil health, irrigation, pests, and farming practices.'
  ),
  sub_agents=[],
  instruction='You are a Crop Knowledge Agent specialized in agricultural advisory.\n\nYour task is to answer farmer questions related to crop cultivation and plant care.\n\nProvide information about:\n• Crop growth requirements\n• Fertilizers and nutrients\n• Soil health\n• Irrigation practices\n• Pest and disease management\n• Farming best practices\n\nWhen answering:\n1. Clearly explain the issue or topic.\n2. Provide practical solutions or recommendations.\n3. Suggest fertilizers, nutrients, or treatments when relevant.\n4. Offer preventive tips to improve crop growth and yield.\n\nKeep responses concise, practical, and easy for farmers to understand.',
  tools=[
    agent_tool.AgentTool(agent=crop_knowledge_agent_google_search_agent),
    agent_tool.AgentTool(agent=crop_knowledge_agent_url_context_agent)
  ],
)
plant_vision_agent_google_search_agent = LlmAgent(
  name='Plant_Vision_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
plant_vision_agent_url_context_agent = LlmAgent(
  name='Plant_Vision_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
plant_vision_agent = LlmAgent(
  name='plant_vision_agent',
  model='gemini-2.5-flash',
  description=(
      'An AI vision agent that analyzes plant or crop images to detect potential plant health issues and provide agricultural insights.'
  ),
  sub_agents=[],
  instruction='You are a Plant Vision Agent.\n\nIf the user uploads an image/video of a plant or crop:\n\n1. Identify the crop if possible\n2. Detect visible symptoms like yellow leaves, spots, pests, wilting\n3. Suggest possible diseases or nutrient deficiencies\n4. Recommend fertilizers or treatments\n5. Provide preventive tips for farmers\n\nIf the image quality is poor, ask the user to upload a clearer image.',
  tools=[
    agent_tool.AgentTool(agent=plant_vision_agent_google_search_agent),
    agent_tool.AgentTool(agent=plant_vision_agent_url_context_agent)
  ],
)
voice_processing_agent_google_search_agent = LlmAgent(
  name='Voice_Processing_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
voice_processing_agent_url_context_agent = LlmAgent(
  name='Voice_Processing_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
voice_processing_agent = LlmAgent(
  name='voice_processing_agent',
  model='gemini-2.5-flash',
  description=(
      'An agent that enables voice interaction by converting farmer speech into text and generating spoken responses.'
  ),
  sub_agents=[],
  instruction='You are a Voice Processing Agent responsible for enabling voice interaction.\n\nYour tasks include:\n1. Converting spoken farmer queries into text using speech recognition.\n2. Send the text query to the Smart Agriculture Assistant\n3. Convert the response into spoken output using Text-to-Speech\n\nEnsure that:\n• Speech recognition captures the farmer\'s intent accurately.\n• Spoken responses are clear, natural, and easy to understand.\n• The interaction remains smooth and conversational.',
  tools=[
    agent_tool.AgentTool(agent=voice_processing_agent_google_search_agent),
    agent_tool.AgentTool(agent=voice_processing_agent_url_context_agent)
  ],
)
agricultural_recommendation_agent_google_search_agent = LlmAgent(
  name='Agricultural_Recommendation_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
agricultural_recommendation_agent_url_context_agent = LlmAgent(
  name='Agricultural_Recommendation_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
agricultural_recommendation_agent = LlmAgent(
  name='agricultural_recommendation_agent',
  model='gemini-2.5-flash',
  description=(
      'An AI agent that generates actionable farming recommendations based on crop questions, plant analysis results, or detected plant health issues.'
  ),
  sub_agents=[],
  instruction='You are an Agricultural Recommendation Agent responsible for providing practical farming guidance.\n\nBased on the input from crop questions or plant image analysis, generate clear recommendations for farmers.\n\nYour response should include:\n1. Explanation of the likely issue affecting the plant or crop.\n2. Recommended fertilizers or nutrients if needed.\n3. Irrigation or soil management suggestions.\n4. Preventive measures to avoid similar problems in the future.\n5. Tips to improve plant health and crop yield.\n\nEnsure recommendations are practical, safe for crops, and easy for farmers to implement.',
  tools=[
    agent_tool.AgentTool(agent=agricultural_recommendation_agent_google_search_agent),
    agent_tool.AgentTool(agent=agricultural_recommendation_agent_url_context_agent)
  ],
)
weather_advisory_agent_google_search_agent = LlmAgent(
  name='Weather_Advisory_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
weather_advisory_agent_url_context_agent = LlmAgent(
  name='Weather_Advisory_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
weather_advisory_agent = LlmAgent(
  name='weather_advisory_agent',
  model='gemini-2.5-flash',
  description=(
      'An agent that provides weather-based farming advice to help farmers make irrigation, fertilization, and crop protection decisions.'
  ),
  sub_agents=[],
  instruction='Use weather data to advise farmers on:\n• irrigation timing\n• pesticide spraying conditions\n• heat stress protection\n• rain risk management',
  tools=[
    agent_tool.AgentTool(agent=weather_advisory_agent_google_search_agent),
    agent_tool.AgentTool(agent=weather_advisory_agent_url_context_agent)
  ],
)
agriculture_product_agent_google_search_agent = LlmAgent(
  name='Agriculture_Product_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
agriculture_product_agent_url_context_agent = LlmAgent(
  name='Agriculture_Product_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
agriculture_product_agent = LlmAgent(
  name='agriculture_product_agent',
  model='gemini-2.5-flash',
  description=(
      'An agent that recommends relevant agricultural products such as fertilizers, pesticides, and farming tools based on crop conditions and provides trusted shopping links.'
  ),
  sub_agents=[],
  instruction='You are an Agriculture Product Recommendation Agent.\n\nYour role is to recommend relevant agricultural products such as fertilizers, pesticides, and crop protection solutions based on the crop issue identified.\n\nWhen providing recommendations:\n1. Suggest appropriate fertilizers, nutrients, pesticides, or farming tools.\n2. Explain briefly why the product is useful for the crop problem.\n3. Provide reliable shopping links where farmers can purchase the product.\n4. Prefer trusted agricultural marketplaces or well-known suppliers.\n\nEnsure recommendations are safe for crops and suitable for the problem identified.\nAvoid suggesting unnecessary or harmful chemicals.\n\nUse GoogleSearchTool to find product purchase links\nfrom trusted agriculture marketplaces like AgroStar,\nBigHaat, Amazon, or Flipkart.',
  tools=[
    agent_tool.AgentTool(agent=agriculture_product_agent_google_search_agent),
    agent_tool.AgentTool(agent=agriculture_product_agent_url_context_agent)
  ],
)
smart_agriculture_assistant_google_search_agent = LlmAgent(
  name='Smart_Agriculture_Assistant_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
smart_agriculture_assistant_url_context_agent = LlmAgent(
  name='Smart_Agriculture_Assistant_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
root_agent = LlmAgent(
  name='Smart_Agriculture_Assistant',
  model='gemini-2.5-flash',
  description=(
      'An AI assistant that helps farmers by answering crop-related questions, analyzing plant images or videos, and providing actionable agricultural recommendations using voice or text interaction.'
  ),
  sub_agents=[crop_knowledge_agent, plant_vision_agent, voice_processing_agent, agricultural_recommendation_agent, weather_advisory_agent, agriculture_product_agent],
  instruction='You are a Smart Agriculture Assistant designed to support farmers with crop-related guidance.\n\nYou can handle different types of inputs including text queries, voice queries, and images or videos of crops or plants.\n\nYour responsibilities include:\n1. Understanding the user\'s request related to crops, plant health, fertilizers, irrigation, pests, or farming practices.\n2. Routing the request to the appropriate specialized agent when needed.\n3. Providing clear and actionable responses that help farmers improve crop health and yield.\n\nYou may use the following specialist agents:\n• Crop Knowledge Agent – for answering crop and farming related questions\n• Plant Vision Agent – for analyzing plant or crop images\n• Voice Processing Agent – for handling speech input and generating spoken responses\n• Agricultural Recommendation Agent – for generating practical farming advice based on analysis\n\nAlways ensure that responses are:\n• Easy to understand\n• Practical and actionable\n• Suitable for farmers with varying levels of technical knowledge\n\nIf the response includes recommendations for fertilizers, pesticides, crop protection products, or farming tools, you MUST consult the Agriculture Product Agent to generate relevant product suggestions and provide shopping links.\n',
  tools=[
    agent_tool.AgentTool(agent=smart_agriculture_assistant_google_search_agent),
    agent_tool.AgentTool(agent=smart_agriculture_assistant_url_context_agent)
  ],
)
