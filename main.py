from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import uvicorn





app = FastAPI()

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ankit@2026",
        database="school_db "
    )
class Student(BaseModel):
    student_id: int
    name: str
    age: int
    gender: str
    class_name: str
    city: str
    marks: int
    admission_date: str


@app.get("/students")
def get_connection():
   db=get_db_connection()
   cursor=db.cursor(dictionary=True)
   cursor.execute("select * from students")
   data=cursor.fetchall()

   cursor.close()
   db.close()
   return data





@app.post("/students")
def add_student(student: Student):

    db=get_db_connection()
    cursor=db.cursor()
    query="""
INSERT INTO students
( student_id,name,age,gender,class,city,marks ,admission_date )
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""
    values = (
        student.student_id,
        student.name,
        student.age,
        student.gender,
        student.class_name,
        student.city,
        student.marks,
        student.admission_date
    )
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Student successfully Added"}


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    db = get_db_connection()
    cursor = db.cursor()

    query = """
    UPDATE students
    SET name=%s,
        age=%s,
        gender=%s,
        class=%s,
        city=%s,
        marks=%s,
        admission_date=%s
    WHERE student_id=%s
    """

    values = (
        student.name,
        student.age,
        student.gender,
        student.class_name,
        student.city,
        student.marks,
        student.admission_date,
        student_id
    )

    cursor.execute(query, values)
    db.commit()

    cursor.close()
    db.close()

    return {"message": "Student Updated Successfully"}

class Students(BaseModel):
    ids:list[int]


@app.delete("/students")
def delete_student(data: Students):
    db = get_db_connection()
    cursor = db.cursor()

    query = "DELETE FROM students WHERE student_id IN( %s,%s,%s)"
    cursor.execute(query,tuple(data.ids) )

    db.commit()

    if cursor.rowcount == 0:
        return {"message": "Student not found"}

    cursor.close()
    db.close()

    return {"message": "Student Deleted Successfully"}


uvicorn.run(app, host="localhost", port=8000)