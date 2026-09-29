from gemini_client import GeminiClient
def explain_topic(client,topic):
    return client.generate(f'''You are EduGenie. Explain this topic to a beginner: {topic}\n\nUse: 1. Simple definition 2. How it works 3. Easy example 4. Important points 5. Short recap. Use simple English.''')
