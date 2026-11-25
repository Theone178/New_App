from pydantic import BaseModel , Field

class EmployeeReq(BaseModel):
    name: str = Field(min_length=1)
    email:str = Field(min_length=1)
    salary:float = Field(gt=0)

class EmployeeResp(BaseModel):
    id:int
    name:str
    email:str
    salary:float
