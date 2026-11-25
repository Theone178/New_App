import logging 
from fastapi import FastAPI , Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from models import Employee
from exceptions import AppException
from service import EmployeeService
from repository import EmployeeRepository
from schemas import EmployeeReq,EmployeeResp

logging.basicConfig(level = logging.INFO,format = "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",)
logger = logging.getLogger("app")

app = FastAPI("Employee_App")

service = EmployeeService(EmployeeRepository())

@app.post("/employees",response_model=EmployeeResp,status_code=201)
def add_emp(req :EmployeeReq):
    return service.creat_Employee(req.name,req.email,req.salary)


@app.get("/employees/{emp_id}",response_model=EmployeeResp)
def get_emp(emp_id):
    return service.get(emp_id)