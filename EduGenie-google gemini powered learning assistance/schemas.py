from typing import List
from pydantic import BaseModel,Field
class QuestionRequest(BaseModel): question:str=Field(...,min_length=1,max_length=10000)
class ExplainRequest(BaseModel): topic:str=Field(...,min_length=1,max_length=5000)
class TextRequest(BaseModel): text:str=Field(...,min_length=1,max_length=20000)
class QuizRequest(BaseModel): text:str=Field(...,min_length=1,max_length=20000); number_of_questions:int=Field(3,ge=1,le=10)
class LearningPathRequest(BaseModel): topic:str=Field(...,min_length=1,max_length=5000); level:str=Field('beginner',min_length=1,max_length=50)
class QuizQuestion(BaseModel): question:str; options:List[str]; correct_answer:str; explanation:str
class QuizResponse(BaseModel): title:str; questions:List[QuizQuestion]
