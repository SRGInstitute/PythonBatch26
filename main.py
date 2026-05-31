from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model
class User(BaseModel):
    name: str
    age: int

# POST API
@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }
#GET API
@app.get("/users")
def get_user():
    return {
        "name": "Sudhish",
        "age": 17
    }
#PUT API
@app.put("/users")
def update_user(user: User):
    return {
        "message": "User updated successfully",
        "updated_data": user
    }
#DELETE API
@app.delete("/users")
def delete_user(user: User):
    return {"message": "User deleted successfully"}