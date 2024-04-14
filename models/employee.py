from pydantic import BaseModel, EmailStr

class Employee(BaseModel):
    employee_id: int
    name: str
    email: EmailStr
    department: str  
    position: str  
    hire_date: str