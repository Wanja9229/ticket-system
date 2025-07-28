class CustomException(Exception):
    def __init__(self, message: str, code: int = 400):
        self.message = message
        self.code = code
        super().__init__(self.message)


class NotFoundException(CustomException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, 404)


class UnauthorizedException(CustomException):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, 401)


class ForbiddenException(CustomException):
    def __init__(self, message: str = "Forbidden"):
        super().__init__(message, 403)


class BadRequestException(CustomException):
    def __init__(self, message: str = "Bad request"):
        super().__init__(message, 400)


class ConflictException(CustomException):
    def __init__(self, message: str = "Conflict"):
        super().__init__(message, 409)
