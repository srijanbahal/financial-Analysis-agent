from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents.data_analyst import get_data_analyst_agent
from agents.trading_strategy import get_trading_strategy_agent
from agents.trade_advisor import get_trade_advisor_agent
from agents.risk_advisor import get_risk_advisor_agent
from tasks1.data_analysis import get_data_analysis_task
from tasks1.strategy_development import get_strategy_development_task
from tasks1.execution_planning import get_execution_planning_task
from tasks1.risk_assesment import get_risk_assessment_task

def run_financial_trading_crew(inputs, progress_callback=None):
    # Instantiate agents
    data_analyst = get_data_analyst_agent()
    trading_strategy = get_trading_strategy_agent()
    trade_advisor = get_trade_advisor_agent()
    risk_advisor = get_risk_advisor_agent()

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
        manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
        process=Process.hierarchical,
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
    result = crew.kickoff(inputs=inputs)
    return result
