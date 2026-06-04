from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

# Apne MySQL username, password aur database name yaha daalo
DATABASE_URL = "mysql+pymysql://root:sudhish%402009@localhost/studentdb"

engine = create_engine(DATABASE_URL)

@app.get("/")
def home():
    return {"message": "FastAPI connected successfully"}

@app.get("/students")
def get_students():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM students"))
        data = [dict(row._mapping) for row in result]
        return data