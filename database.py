from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:Arjunpandat%4052@localhost/studentpdb"
engine = create_engine(DATABASE_URL)

class Student(BaseModel):
    name: str
    age: int


# GET
@app.get("/students")
def get_students():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM students"))
        students = [dict(row._mapping) for row in result]
        return students


# POST
@app.post("/students")
def add_student(student: Student):
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO students (name, age) VALUES (:name, :age)"),
            {"name": student.name, "age": student.age}
        )
        conn.commit()
    return {"message": "Student added successfully"}


# PUT
@app.put("/students/{id}")
def update_student(id: int, student: Student):
    with engine.connect() as conn:
        conn.execute(
            text("""
                UPDATE students
                SET name=:name, age=:age
                WHERE id=:id
            """),
            {
                "id": id,
                "name": student.name,
                "age": student.age
            }
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