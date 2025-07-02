from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

def get_data_analyst_agent():
    return Agent(
        role="Data Analyst",
        goal="Monitor and analyze market data in real-time to identify trends and predict market movements.",
        backstory="Specializing in financial markets, this agent uses statistical modeling and machine learning to provide crucial insights. With a knack for data, the Data Analyst Agent is the cornerstone for informing trading decisions.",
        verbose=True,
        allow_delegation=True,
        tools=[ScrapeWebsiteTool(), SerperDevTool()]
    )
