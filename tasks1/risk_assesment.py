from crewai import Task

def get_risk_assessment_task(agent, stock_selection):
    return Task(
        description=(
            f"Evaluate the risks associated with the proposed trading strategies and execution plans for {stock_selection}. "
            "Provide a detailed analysis of potential risks and suggest mitigation strategies."
        ),
        expected_output=(
            f"A comprehensive risk analysis report detailing potential risks and mitigation recommendations for {stock_selection}."
        ),
        agent=agent,
    )
