# EduGenie

Root-level FastAPI educational assistant with Q&A, explanation, quizzes, summaries and learning paths.

## Run on Windows

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000

The included `.env` starts in MOCK_AI mode, so no API key is required for testing. To use Gemini, set `GEMINI_API_KEY` and `MOCK_AI=false`.
