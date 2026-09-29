import json
from google import genai
from google.genai import types
from config import settings
class GeminiClient:
    def __init__(self):
        self.mock=settings.MOCK_AI; self.model=settings.GEMINI_MODEL; self.client=None
        if not self.mock:
            if not settings.GEMINI_API_KEY: raise RuntimeError('GEMINI_API_KEY is missing. Set it in .env or use MOCK_AI=true.')
            self.client=genai.Client(api_key=settings.GEMINI_API_KEY)
    def generate(self,prompt):
        if self.mock: return self._mock(prompt)
        r=self.client.models.generate_content(model=self.model,contents=prompt)
        if not getattr(r,'text',None): raise RuntimeError('Gemini returned an empty response.')
        return r.text.strip()
    def generate_json(self,prompt):
        if self.mock: return json.loads(self._mock(prompt))
        r=self.client.models.generate_content(model=self.model,contents=prompt,config=types.GenerateContentConfig(response_mime_type='application/json'))
        if not getattr(r,'text',None): raise RuntimeError('Gemini returned an empty JSON response.')
        try: return json.loads(r.text)
        except json.JSONDecodeError as e: raise ValueError(f'Gemini returned invalid JSON: {e}') from e
    def _mock(self,prompt):
        p=prompt.lower()
        if 'multiple-choice' in p or 'mcq' in p:
            n=3
            marker='exactly '
            i=p.find(marker)
            if i>=0:
                digits=''
                for c in p[i+len(marker):]:
                    if c.isdigit(): digits+=c
                    else: break
                if digits: n=max(1,min(10,int(digits)))
            bank=[
              ('What is SQL mainly used for?',['Managing relational data','Editing photos','Creating music','Designing hardware'],'Managing relational data','SQL manages data in relational databases.'),
              ('Which SQL command retrieves data?',['SELECT','DELETE','DROP','CREATE'],'SELECT','SELECT retrieves rows from tables.'),
              ('What does DBMS stand for?',['Database Management System','Data Backup Management Software','Digital Business Management Service','Database Machine System'],'Database Management System','DBMS means Database Management System.'),
              ('Which keyword filters rows?',['WHERE','ORDER','GROUP','JOIN'],'WHERE','WHERE applies row conditions.'),
              ('Which command adds rows?',['INSERT','UPDATE','DELETE','SELECT'],'INSERT','INSERT adds new records.'),
              ('Which command changes rows?',['UPDATE','INSERT','CREATE','SELECT'],'UPDATE','UPDATE changes existing records.'),
              ('Which command removes rows?',['DELETE','DROP ROW','CLEAR','ERASE'],'DELETE','DELETE removes selected records.'),
              ('What is a primary key?',['A unique row identifier','A password','A backup','A chart'],'A unique row identifier','A primary key uniquely identifies a row.')]
            qs=[]
            for j in range(n):
                q=bank[j%len(bank)]; qs.append({'question':q[0],'options':q[1],'correct_answer':q[2],'explanation':q[3]})
            return json.dumps({'title':'EduGenie Sample Quiz','questions':qs})
        if 'learning path' in p: return '# Learning Path\n\n## Beginner\n- Learn fundamentals.\n- Practice simple examples.\n\n## Intermediate\n- Learn practical techniques.\n- Build projects.\n\n## Advanced\n- Study advanced concepts.\n- Optimize and apply best practices.\n\n## Timeline\n- Weeks 1-2: Fundamentals\n- Weeks 3-4: Intermediate\n- Weeks 5-8: Projects and advanced topics.'
        if 'summar' in p: return 'Sample summary from MOCK_AI mode. Disable MOCK_AI and add a Gemini API key for real summaries.'
        if 'explain' in p: return 'Sample explanation from MOCK_AI mode. Disable MOCK_AI and add a Gemini API key for real explanations.'
        return 'Sample EduGenie answer from MOCK_AI mode. Disable MOCK_AI and add a Gemini API key for real Gemini responses.'
