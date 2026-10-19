from multi_agent_acl.prompt import WEDDING_PLANNER_AGENT_PROMP, USER_PROMPT_FOR_MAIN_AGENT
from langchain.agents import create_agent
from multi_agent_acl.models import ai_model
from multi_agent_acl.agents import delegate_to_subagent1,delegate_to_subagent2
import logging
import sys
from langchain.messages import HumanMessage


def main() -> None:
    # LLM output often has unicode (dashes, emoji); Windows defaults to cp1252 when output is redirected
    sys.stdout.reconfigure(encoding="utf-8")

    #configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        force=True  # a library already set up logging on import; replace its config with ours
    )

    #asking user for their requirements for there wedding
    logging.info("asking the user for their requirements...")
    user_requirements = input("Please enter your requirements and preferences for your wedding\n")

    #updating the system prompt
    updaed_system_prompt = WEDDING_PLANNER_AGENT_PROMP.format(requirements=user_requirements)

    # creating the main agent
    logging.info("initializing main wedding planner agent...")
    main_wedding_planner_agent = create_agent(model=ai_model,tools=[delegate_to_subagent1,delegate_to_subagent2],name="MainWeddingPlannerAgent",system_prompt=updaed_system_prompt)

    # imvoke main agent
    logging.info("invoking main wedding planner agent...")
    response_main_agent = main_wedding_planner_agent.invoke({"messages":[HumanMessage(USER_PROMPT_FOR_MAIN_AGENT)]})

    # print the response of the main agent
    print("\n Main Wedding Planner Agent's response: ")
    print(response_main_agent["messages"][-1].content)
