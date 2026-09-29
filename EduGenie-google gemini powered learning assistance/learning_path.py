from gemini_client import GeminiClient
def get_learning_recommendations(client,topic,level):
    return client.generate(f'''You are EduGenie, a learning-path assistant. Create a practical progression for {topic}. Current level: {level}. Include prerequisites, beginner/intermediate/advanced topics, timeline, practice activities, project ideas, resource types, milestones, and revision strategy. Do not invent specific URLs.''')
