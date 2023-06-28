from pydantic import BaseModel

class Student(BaseModel):
    id: str
    name: str
    mobile_number: str

