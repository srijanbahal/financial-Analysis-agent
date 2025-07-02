# Multi-Agent Financial Analysis Bot

## Features
- Modular agent/task structure using crewAI
- Streamlit frontend for manual or PDF input (with OCR)
- Real-time agent progress visualization
- Extensible and maintainable codebase

## Setup
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your API keys as environment variables:
   - `OPENAI_API_KEY`
   - `SERPER_API_KEY`
3. Run the frontend:
   ```bash
   streamlit run frontend/app.py
   ```
4. Or run the CLI demo:
   ```bash
   python main.py
   ```

## Project Structure
- `agents/` - Agent definitions
- `tasks1/` - Task definitions
- `crew/` - Crew orchestration
- `utils/` - Utilities (API keys, OCR)
- `frontend/` - Streamlit app
- `main.py` - CLI entry point
- `config.py` - Configuration
- `requirements.txt` - Dependencies
- `README.md` - This file

## Notes
- For PDF input, fields are extracted via OCR and can be manually corrected in the UI.
- The backend supports progress callbacks for real-time UI updates.
