from src.models import TasksORM
from src.repositories.mappers.base import DataMapper
from src.schemas.tasks import Task


class TaskDataMapper(DataMapper):
    db_model = TasksORM
    schema = Task
