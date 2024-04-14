# Employee Shift Management API

## Prerequisites
- Python 3.x
- Pipenv (to install, run `pip install pipenv`)

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>

Navigate to the project directory:

Bash
cd employee-shift-management-api
Use code with caution.
Install dependencies using Pipenv:
Bash
# pipenv install

Activate Virtual Environment
To activate the virtual environment created by Pipenv, run:

# Bash
pipenv shell

Running the API
To start the FastAPI application, run:

Bash
# uvicorn main:app --reload

# The API will be accessible at http://localhost:8000.

Testing Endpoints
Employee Management

Add a new employee:

# URL: http://localhost:8000/employees/
Method: POST
Request Body (JSON):
# JSON
{
  "employee_id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "department": "Engineering",
  "position": "Software Engineer",
  "hire_date": "2022-01-01"
}
#
## Expected Response: The details of the newly created employee.
Retrieve a list of all employees:

# URL: http://localhost:8000/employees/
Method: GET
Expected Response: A list of all employees.
Retrieve details of a specific employee:
#
# URL: http://localhost:8000/employees/{employee_id}
# Method: GET
Expected Response: The details of the specific employee with the given employee ID.
Update the details of a specific employee:
#
## URL: http://localhost:8000/employees/{employee_id}
Method: PUT
Request Body: Updated details of the employee (JSON format).
Expected Response: A message indicating successful update.
Delete a specific employee:
##
# URL: http://localhost:8000/employees/{employee_id}
Method: DELETE
Expected Response: A message indicating successful deletion.
Shift Management
##
Assign a new shift to an employee:

# URL: http://localhost:8000/shifts/
Method: POST
Request Body (JSON):
JSON
{
  "shift_id": 1,
  "employee_id": 1,
  "start_time": "08:00",
  "end_time": "16:00",
  "shift_date": "2024-04-14",
  "location": "Office",
  "role": "Software Development"
}
##
Expected Response: The details of the newly assigned shift.
Retrieve a list of all shifts:

# URL: http://localhost:8000/shifts/
Method: GET
Expected Response: A list of all shifts.
Retrieve details of a specific shift:
##
# URL: http://localhost:8000/shifts/{shift_id}
Method: GET
Expected Response: The details of the specific shift with the given shift ID.
Update a specific shift:
##
# URL: http://localhost:8000/shifts/{shift_id}
Method: PUT
Request Body: Updated details of the shift (JSON format).
Expected Response: A message indicating successful update.
Delete a specific shift:
##
# URL: http://localhost:8000/shifts/{shift_id}
Method: DELETE
Expected Response: A message indicating successful deletion.
Additional Endpoints
##
Retrieve all shifts assigned to a specific employee:

# URL: http://localhost:8000/employees/{employee_id}/shifts
Method: GET
Expected Response: A list of all shifts assigned to the specific employee with the given employee ID.
##