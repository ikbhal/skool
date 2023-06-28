from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv
from models import Student


app = FastAPI()
load_dotenv()

# MongoDB Configuration
client = MongoClient(environ.get("MONGODB_URI"))
db = client[environ.get("MONGODB_DATABASE")]
students_collection = db["students"]


@app.post("/students")
async def add_student(student: Student):
    students_collection.insert_one(student.dict())
    return {"message": "Student added successfully!"}


@app.get("/students/{mobile_number}")
async def get_student(mobile_number: str):
    student = students_collection.find_one({"mobile_number": mobile_number})
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")
