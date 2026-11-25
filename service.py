import logging
from exceptions import ConflictError, NotFoundError
from models import Employee
from repository import EmployeeRepository

logger = logging.getLogger("App")

class EmployeeService:
    def __init__(self,repo:EmployeeRepository):
        self._repo=repo

    def creat_Employee(self,name:str,email:str,salary:float)->Employee:
        email = email.strip().lower()
        if(self._repo.find_by_email(email)):
            logger.warning("Duplicate email rejected: email=%s",email)
            raise ConflictError(f"Email {email} already exists")
        emp = self._repo.save(name.strip(),email,salary)
        logger.info("Added employee: id = %s",emp.id)
        return emp

    def get(self,emp_id:int)->Employee:
            emp = self._repo.find_by_id(emp_id)
            if emp is None :
                logger.warning("Employee not found: id=%s", emp_id)
                raise NotFoundError(f"Employee {emp_id} not found")
            return emp