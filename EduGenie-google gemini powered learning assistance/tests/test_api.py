import os
os.environ['MOCK_AI']='true'
from fastapi.testclient import TestClient
from main import app
client=TestClient(app)
def test_health(): assert client.get('/health').status_code==200
def test_home(): assert 'EduGenie' in client.get('/').text
def test_qa(): assert client.post('/qa',json={'question':'What is SQL?'}).status_code==200
def test_explain(): assert client.post('/explain',json={'topic':'SQL'}).status_code==200
def test_summary(): assert client.post('/summarize',json={'text':'SQL manages relational data.'}).status_code==200
def test_learning(): assert client.post('/learn/recommendations',json={'topic':'Python','level':'beginner'}).status_code==200
def test_quiz():
 r=client.post('/quiz',json={'text':'SQL manages databases.','number_of_questions':5}); assert r.status_code==200 and len(r.json()['questions'])==5
