import threading
from models import Employee

class EmployeeRepository:
    def __init__(self):
        self._data : dict[int,Employee] = {}
        self._next_id = 1 
        self._lock = threading.Lock()

    def save(self,name:str,email:str,salary:float)->Employee:
        with self._lock :
            emp = Employee(self._next_id,name,email,salary) 
            self._data[self._next_id] = emp
            _next_id +=1
            return emp

    def find_by_id(self, emp_id:int)->Employee | None:
        return self._data.get(emp_id)

    def find_by_email(self,email:str)->Employee | None :
        return next((e for e in self._data.values() if e.email == email ),None)