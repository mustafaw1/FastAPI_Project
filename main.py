# main.py

from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import ValidationError
from models.employee import Employee
from models.shift import Shift

app = FastAPI(
    title="Employee and Shift Management API",
    description="API for managing employees and their shifts",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)

# Dummy data to simulate database
employees_db = []
shifts_db = []

# Employee Management Endpoints
@app.post("/employees/", response_model=Employee, tags=["Employees"])
def create_employee(employee: Employee):
    try:
        new_employee = Employee(**employee.dict())
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    
    employees_db.append(new_employee)
    return new_employee

@app.get("/employees/", response_model=List[Employee], tags=["Employees"])
def get_employees():
    return employees_db

@app.get("/employees/{employee_id}", response_model=Employee, tags=["Employees"])
def get_employee(employee_id: int):
    for employee in employees_db:
        if employee.employee_id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{employee_id}", tags=["Employees"])
def update_employee(employee_id: int, employee: Employee):
    for i, emp in enumerate(employees_db):
        if emp.employee_id == employee_id:
            try:
                employee.validate_email()
            except ValidationError:
                raise HTTPException(status_code=400, detail="Invalid email format")
            employees_db[i] = employee
            return {"message": "Employee updated successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employees/{employee_id}", tags=["Employees"])
def delete_employee(employee_id: int):
    for i, employee in enumerate(employees_db):
        if employee.employee_id == employee_id:
            del employees_db[i]
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")

# Shift Management Endpoints
@app.post("/shifts/", response_model=Shift, tags=["Shifts"])
def assign_shift(shift: Shift):
    for existing_shift in shifts_db:
        if existing_shift.employee_id == shift.employee_id and \
                existing_shift.shift_date == shift.shift_date and \
                (shift.start_time < existing_shift.end_time and shift.end_time > existing_shift.start_time):
            raise HTTPException(status_code=400, detail="Shift overlaps with another shift for the same employee")

    shifts_db.append(shift)
    return shift

@app.get("/shifts/", response_model=List[Shift], tags=["Shifts"])
def get_shifts():
    return shifts_db

@app.get("/shifts/{shift_id}", response_model=Shift, tags=["Shifts"])
def get_shift(shift_id: int):
    for shift in shifts_db:
        if shift.shift_id == shift_id:
            return shift
    raise HTTPException(status_code=404, detail="Shift not found")

@app.put("/shifts/{shift_id}", tags=["Shifts"])
def update_shift(shift_id: int, shift: Shift):
    for i, existing_shift in enumerate(shifts_db):
        if existing_shift.shift_id == shift_id:
            for existing_shift in shifts_db:
                if existing_shift.employee_id == shift.employee_id and \
                        existing_shift.shift_date == shift.shift_date and \
                        (shift.start_time < existing_shift.end_time and shift.end_time > existing_shift.start_time):
                    raise HTTPException(status_code=400, detail="Shift overlaps with another shift for the same employee")
            shifts_db[i] = shift
            return {"message": "Shift updated successfully"}
    raise HTTPException(status_code=404, detail="Shift not found")

@app.delete("/shifts/{shift_id}", tags=["Shifts"])
def delete_shift(shift_id: int):
    for i, shift in enumerate(shifts_db):
        if shift.shift_id == shift_id:
            del shifts_db[i]
            return {"message": "Shift deleted successfully"}
    raise HTTPException(status_code=404, detail="Shift not found")

# Additional Endpoints
@app.get("/employees/{employee_id}/shifts", tags=["Employees"])
def get_employee_shifts(employee_id: int):
    employee_shifts = [shift for shift in shifts_db if shift.employee_id == employee_id]
    if not employee_shifts:
        raise HTTPException(status_code=404, detail="No shifts found for this employee")
    return employee_shifts

@app.get("/shifts/filter/", tags=["Shifts"])
def filter_shifts(date: Optional[str] = None):
    if date:
        filtered_shifts = [shift for shift in shifts_db if shift.shift_date == date]
        return filtered_shifts
    return shifts_db


__all__ = ["app", "TestClient"]
