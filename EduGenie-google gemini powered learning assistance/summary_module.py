from gemini_client import GeminiClient
def summarize_text(client,text):
    return client.generate(f'''You are EduGenie. Summarize this educational text for quick revision. Keep important information and technical terms, remove repetition, and use headings or bullets where useful.\n\n{text}''')
