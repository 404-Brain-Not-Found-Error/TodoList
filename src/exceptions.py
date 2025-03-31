from fastapi import HTTPException


class ZadachiException(Exception):
    detail = "Неожиданная ошибка"

    def __init__(self, *args, **kwargs):
        super().__init__(self.detail, *args, **kwargs)


class ObjectNotFoundException(ZadachiException):
    detail = "Объект не найден"


class TaskNotFoundException(ObjectNotFoundException):
    detail = "Задача не найдена"


class ZadachiHTTPException(HTTPException):
    status_code = 500
    detail = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class TaskNotFoundHTTPException(ZadachiHTTPException):
    status_code = 404
    detail = "Задача не найдена"