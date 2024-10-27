from lyzr_agent_api.client import AgentAPI
from lyzr_agent_api.models.environment import EnvironmentConfig, FeatureConfig
from lyzr_agent_api.models.agents import AgentConfig
from lyzr_agent_api.models.chat import ChatRequest

client = AgentAPI(x_api_key="Lyzr-API-KEY")

environment_config = EnvironmentConfig(
       name="Github Environment",
       features=[
           FeatureConfig(
               type="TOOL_CALLING",
               config={"max_tries": 3},
               priority=0,
           )
       ],
       tools=["get_pr_files","update_pr_description"],
       llm_config={
           "provider": "openai",
           "model": "gpt-4o-mini",
           "config": {
               "temperature": 0.5,
               "top_p": 0.9
           },
           "env": {
               "OPENAI_API_KEY": "OPENAI_API_KEY"
           }
       },
   )

environment = client.create_environment_endpoint(json_body=environment_config)
print(environment['environment_id']) #e.g {'environment_id':'6adnndbnxxxxxxx'}

agent_config = AgentConfig(
       env_id=environment['environment_id'],  #{'environment_id':'6adnndbnxxxxxxx'}
       system_prompt="""
       You are an Github PR assistant. Your Task Is To analyze PR request, code changes and Craft well structures and easy to understandable PR description.

        follow below Instruction Step By Step:
        1) User Gives you a github PR Link and you hava to use get_pr_files tool to fetch PR details for that specific link
        2) This gives you a Changes among the file and you have to Analyze that changes and Create Well structured PR Description for that code changes with bullet point. make it in 2-8 bullet points.
        3) Use update_pr_description tool to update PR description using crafted Description.""",
       name="Newsletter Agent",
       agent_description="This Agent research and craft newsletter on given topic.",
   )

agent = client.create_agent_endpoint(json_body=agent_config)
print(agent['agent_id']) #e.g {'agent_id':'6bdsjdjxxxxxxx'}