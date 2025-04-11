import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.schema import SystemMessage
from langchain_openai import ChatOpenAI

from tools.tools import tools

load_dotenv()
api_key = os.getenv('OPENAI_KEY', 'XXX')

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", api_key=api_key)

agent_kwargs = {
    "system_message": SystemMessage(
        content="""You are a helpful assistant for a bus rental service. Your goal is to help customers:
        1. First check if their pickup location is serviceable
        2. Then check if their desired route (pickup to dropoff) is serviceable
        3. Finally provide a price estimate based on number of passengers
        
        Always follow this exact sequence. Never ask for all information at once.
        Start by asking for pickup location only."""
    ),
    "extra_prompt_messages": [MessagesPlaceholder(variable_name="chat_history")]
}

agent_executor = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
    memory=memory,
    agent_kwargs=agent_kwargs
)