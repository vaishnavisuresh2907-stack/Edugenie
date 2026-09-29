from schemas import QuizResponse
from gemini_client import GeminiClient
def generate_quiz(client,text,number_of_questions=3):
    data=client.generate_json(f'''You are EduGenie, an educational quiz generator. Create EXACTLY {number_of_questions} multiple-choice questions based only on this content:\n{text}\nReturn JSON with title and questions. Each question must have exactly 4 options, exactly one correct_answer matching an option, and an explanation. Do not add extra fields.''')
    quiz=QuizResponse.model_validate(data)
    if len(quiz.questions)!=number_of_questions: raise ValueError(f'Expected {number_of_questions} questions, got {len(quiz.questions)}.')
    for q in quiz.questions:
        if len(q.options)!=4: raise ValueError('Every question must have exactly 4 options.')
        if q.correct_answer not in q.options: raise ValueError('Correct answer must match an option.')
    return quiz
