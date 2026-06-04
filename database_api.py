from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:sudhish%402009@localhost/studentdb"

engine = create_engine(DATABASE_URL)

# GET ALL
@app.get("/students")
def get_students():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM students"))
        return [dict(row._mapping) for row in result]

# POST
@app.post("/students")
def add_student(id: int, name: str):
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO students (id, name) VALUES (:id, :name)"),
            {"id": id, "name": name}
        )
        conn.commit()
    return {"message": "Student added successfully"}

# PUT
@app.put("/students/{id}")
def update_student(id: int, name: str):
    with engine.connect() as conn:
        conn.execute(
            text("UPDATE students SET name=:name WHERE id=:id"),
            {"id": id, "name": name}
        )
        conn.commit()
    return {"message": "Student updated successfully"}

# DELETE
@app.delete("/students/{id}")
def delete_student(id: int):
    with engine.connect() as conn:
        conn.execute(
            text("DELETE FROM students WHERE id=:id"),
            {"id": id}
        )
        conn.commit()
    return {"message": "Student deleted successfully"}