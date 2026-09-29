from gemini_client import GeminiClient
def answer_question(client,question):
    return client.generate(f'''You are EduGenie, an educational AI assistant. Answer accurately and clearly. Give a direct answer first, explain simply, use examples when useful, and do not invent facts.\n\nStudent question:\n{question}''')
