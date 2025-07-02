from crewai import Task

def get_strategy_development_task(agent, stock_selection, risk_tolerance, trading_strategy_preference):
    return Task(
        description=(
            f"Develop and refine trading strategies based on the insights from the Data Analyst and user-defined risk tolerance ({risk_tolerance}). "
            f"Consider trading preferences ({trading_strategy_preference})."
        ),
        expected_output=(
            f"A set of potential trading strategies for {stock_selection} that align with the user's risk tolerance."
        ),
        agent=agent,
    )
