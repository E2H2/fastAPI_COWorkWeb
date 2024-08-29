from models import Question, Answer
from datetime import datetime
from database import SessionLocal
db = SessionLocal()
q = db.query(Question).get(2)
q.subject = 'FastAPI Model Question'
db.commit()
