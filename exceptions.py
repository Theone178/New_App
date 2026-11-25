class AppException(Exception):
    status_code = 500
    code = "Internal Error"

    def __init__(self,message:str):
        super.__init__(message)
        self.message = message 

class BusinessRuleError(AppException):
    status_code = 400
    code ="BAD_REQUEST"

class NotFoundError(AppException):
    status_code = 404
    code = "NOT_FOUND"

class ConflictError(AppException):
    status_code = 409
    code = "CONFLICT"