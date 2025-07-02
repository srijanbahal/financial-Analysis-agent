from crewai import Task

def get_data_analysis_task(agent, stock_selection):
    return Task(
        description=(
            f"Continuously monitor and analyze market data for the selected stock ({stock_selection}). "
            "Use statistical modeling and machine learning to identify trends and predict market movements."
        ),
        expected_output=(
            f"Insights and alerts about significant market opportunities or threats for {stock_selection}."
        ),
        agent=agent,
    )
