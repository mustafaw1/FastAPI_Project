from pydantic import BaseModel
from models.employee import Employee

class Shift(BaseModel):
    shift_id: int
    employee_id: int
    start_time: str
    end_time: str
    shift_date: str
    location: str  
    role: str  

    def employee(self):
        return Employee.get(self.employee_id)