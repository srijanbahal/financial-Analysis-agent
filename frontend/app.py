import streamlit as st
import sys
import os
import chromadb.utils.embedding_functions as ef

# Overwrite default embedding function
ef.DefaultEmbeddingFunction = lambda: ef.ONNXMiniLM_L6_V2()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.ocr import extract_text_from_pdf
from crew.financial_trading_crew import run_financial_trading_crew

st.title("Multi-Agent Financial Analysis Bot")

st.header("Enter Trading Inputs")
input_method = st.radio("Input Method", ["Manual Entry", "Upload PDF"])

user_inputs = {}

if input_method == "Manual Entry":
    stock = st.text_input("Stock Symbol", "AAPL")
    capital = st.text_input("Initial Capital", "100000")
    risk = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
    strategy = st.selectbox("Trading Strategy", ["Day Trading", "Swing Trading", "Long Term"])
    news_impact = st.checkbox("Consider News Impact", value=True)
    user_inputs = {
        'stock_selection': stock,
        'initial_capital': capital,
        'risk_tolerance': risk,
        'trading_strategy_preference': strategy,
        'news_impact_consideration': news_impact
    }
elif input_method == "Upload PDF":
    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
    if pdf_file:
        text = extract_text_from_pdf(pdf_file.read())
        st.text_area("Extracted Text", value=text, height=200)
        # For demo, let user manually fill fields after seeing extracted text
        stock = st.text_input("Stock Symbol", "AAPL")
        capital = st.text_input("Initial Capital", "100000")
        risk = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
        strategy = st.selectbox("Trading Strategy", ["Day Trading", "Swing Trading", "Long Term"])
        news_impact = st.checkbox("Consider News Impact", value=True)
        user_inputs = {
            'stock_selection': stock,
            'initial_capital': capital,
            'risk_tolerance': risk,
            'trading_strategy_preference': strategy,
            'news_impact_consideration': news_impact
        }

if user_inputs and st.button("Run Analysis"):
    progress_bar = st.progress(0)
    status = st.empty()
    agent_steps = [
        "Data Analyst",
        "Trading Strategy Developer",
        "Trade Advisor",
        "Risk Advisor"
    ]
    def progress_callback(step, agent, msg):
        progress_bar.progress(step / len(agent_steps))
        status.info(f"{agent} is working: {msg}")
    result = run_financial_trading_crew(user_inputs, progress_callback=progress_callback)
    progress_bar.progress(1.0)
    status.success("Analysis Complete!")
    st.markdown(result)
