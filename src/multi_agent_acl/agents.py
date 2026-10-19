from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from multi_agent_acl.models import ai_model
from multi_agent_acl.tools import search_web
import logging

# creating subagents
logging.info("initializing SubAgent1 ...")
subagent1 = create_agent(model=ai_model, tools=[search_web], name='SubAgent1')

logging.info("initializing SubAgent2 ...")
subagent2 = create_agent(model=ai_model, tools=[search_web], name='SubAgent2')

@tool
def delegate_to_subagent1(query:str)->str:
    """Search the web for a given topic by deligating a task to Subagent1 to do so"""
    logging.info(f"Delegating query to SubAgent1: {query}")
    response = subagent1.invoke({"messages":[HumanMessage(content=query)]})
    return response["messages"][-1].content

@tool
def delegate_to_subagent2(query:str)->str:
    """Search the web for a given topic by deligating a task to Subagent2 to do so"""
    logging.info(f"Delegating query to SubAgent2: {query}")
    response = subagent2.invoke({"messages":[HumanMessage(content=query)]})
    return response["messages"][-1].content