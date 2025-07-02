from crewai import Task

def get_execution_planning_task(agent, stock_selection):
    return Task(
        description=(
            f"Analyze approved trading strategies to determine the best execution methods for {stock_selection}, "
            "considering current market conditions and optimal pricing."
        ),
        expected_output=(
            f"Detailed execution plans suggesting how and when to execute trades for {stock_selection}."
        ),
        agent=agent,
    )
