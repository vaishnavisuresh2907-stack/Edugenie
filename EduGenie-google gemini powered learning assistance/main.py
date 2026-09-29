from pathlib import Path
from fastapi import Depends,FastAPI,HTTPException,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config import settings
from dependencies import get_gemini_client
from gemini_client import GeminiClient
from schemas import QuestionRequest,ExplainRequest,TextRequest,QuizRequest,QuizResponse,LearningPathRequest
from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations
BASE_DIR=Path(__file__).resolve().parent
app=FastAPI(title=settings.APP_NAME,version='1.0.0')
app.mount('/static',StaticFiles(directory=str(BASE_DIR/'static')),name='static')
templates=Jinja2Templates(directory=str(BASE_DIR/'templates'))
@app.get('/',response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"app_name": settings.APP_NAME},
    )

@app.get('/health')
async def health(): return {'status':'ok','app':settings.APP_NAME,'mock_ai':settings.MOCK_AI,'model':settings.GEMINI_MODEL}
@app.post('/qa')
async def qa(request:QuestionRequest,client:GeminiClient=Depends(get_gemini_client)):
    try:return {'success':True,'answer':answer_question(client,request.question)}
    except Exception as e: raise HTTPException(500,str(e)) from e
@app.post('/explain')
async def explain(request:ExplainRequest,client:GeminiClient=Depends(get_gemini_client)):
    try:return {'success':True,'explanation':explain_topic(client,request.topic)}
    except Exception as e: raise HTTPException(500,str(e)) from e
@app.post('/quiz',response_model=QuizResponse)
async def quiz(request:QuizRequest,client:GeminiClient=Depends(get_gemini_client)):
    try:return generate_quiz(client,request.text,request.number_of_questions)
    except Exception as e: raise HTTPException(500,str(e)) from e
@app.post('/summarize')
async def summarize(request:TextRequest,client:GeminiClient=Depends(get_gemini_client)):
    try:return {'success':True,'summary':summarize_text(client,request.text)}
    except Exception as e: raise HTTPException(500,str(e)) from e
@app.post('/learn/recommendations')
async def learn(request:LearningPathRequest,client:GeminiClient=Depends(get_gemini_client)):
    try:return {'success':True,'recommendations':get_learning_recommendations(client,request.topic,request.level)}
    except Exception as e: raise HTTPException(500,str(e)) from e
