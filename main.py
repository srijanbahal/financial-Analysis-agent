from crew.financial_trading_crew import run_financial_trading_crew

def main():
    user_inputs = {
        'stock_selection': 'AAPL',
        'initial_capital': '100000',
        'risk_tolerance': 'Medium',
        'trading_strategy_preference': 'Day Trading',
        'news_impact_consideration': True
    }
    def progress_callback(step, agent, msg):
        print(f"Step {step}: {agent} - {msg}")
    result = run_financial_trading_crew(user_inputs, progress_callback=progress_callback)
    print("\nFinal Result:\n", result)

if __name__ == "__main__":
    main()
