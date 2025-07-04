from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

def get_trading_strategy_agent(llm):
    return Agent(
        role="Trading Strategy Developer",
        goal="Develop and test various trading strategies based on insights from the Data Analyst Agent.",
        backstory="Equipped with a deep understanding of financial markets and quantitative analysis, this agent devises and refines trading strategies. It evaluates the performance of different approaches to determine the most profitable and risk-averse options.",
        verbose=True,
        allow_delegation=True,
        tools=[ScrapeWebsiteTool(), SerperDevTool()],
        llm=llm
    )
