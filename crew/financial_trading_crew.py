from crewai import Crew, Process
from agents.data_analyst import get_data_analyst_agent
from agents.trading_strategy import get_trading_strategy_agent
from agents.trade_advisor import get_trade_advisor_agent
from agents.risk_advisor import get_risk_advisor_agent
from tasks1.data_analysis import get_data_analysis_task
from tasks1.strategy_development import get_strategy_development_task
from tasks1.execution_planning import get_execution_planning_task
from tasks1.risk_assesment import get_risk_assessment_task
from llm_wrappers.manager_llm_wrapper import ManagerLLMWrapper
from utils.token_utils import count_tokens, trim_text_to_token_limit
from crewai import LLM
from dotenv import load_dotenv
import os

load_dotenv()

# Your OpenRouter base model
base_llm = LLM(
    model="mistralai/mistral-small-3.2-24b-instruct:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",  # this tells LiteLLM the provider implicitly
    litellm_params={ "api_base": "https://openrouter.ai/api/v1", "api_key": os.getenv("OPENROUTER_API_KEY") }
)
# Wrap it with manager wrapper
manager_llm = ManagerLLMWrapper(
    base_llm=base_llm,
    max_tokens=80000,
    model_name="openrouter/mistralai/mistral-small-3.2-24b-instruct:free"  # purely for tokenizer compatibility
)



def run_financial_trading_crew(inputs, progress_callback=None):
    # Instantiate agents
    data_analyst = get_data_analyst_agent(llm=manager_llm)
    trading_strategy = get_trading_strategy_agent(llm=manager_llm)
    trade_advisor = get_trade_advisor_agent(llm=manager_llm)
    risk_advisor = get_risk_advisor_agent(llm=manager_llm)

    # Instantiate tasks
    data_analysis_task = get_data_analysis_task(data_analyst, inputs['stock_selection'])
    strategy_development_task = get_strategy_development_task(
        trading_strategy,
        inputs['stock_selection'],
        inputs['risk_tolerance'],
        inputs['trading_strategy_preference']
    )
    execution_planning_task = get_execution_planning_task(trade_advisor, inputs['stock_selection'])
    risk_assessment_task = get_risk_assessment_task(risk_advisor, inputs['stock_selection'])

    # Create crew
    crew = Crew(
        agents=[data_analyst, trading_strategy, trade_advisor, risk_advisor],
        tasks=[data_analysis_task, strategy_development_task, execution_planning_task, risk_assessment_task],
        manager_llm=manager_llm,
        process=Process.sequential,
        verbose=True
    )

    # Simulate progress reporting
    steps = [
        ("Data Analyst", "Analyzing market data..."),
        ("Trading Strategy Developer", "Developing trading strategies..."),
        ("Trade Advisor", "Planning trade execution..."),
        ("Risk Advisor", "Assessing trading risks...")
    ]
    for i, (agent, msg) in enumerate(steps, 1):
        if progress_callback:
            progress_callback(i, agent, msg)

    # Run the crew
    print("Model being used:", manager_llm.model_name)
    # if manager_llm.model_name == base_llm:
    #     result = crew.kickoff(inputs=inputs)
    result = crew.kickoff(inputs=inputs)
    return result
