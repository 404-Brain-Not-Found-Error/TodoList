from src.models import TasksORM
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import TaskDataMapper


class TasksRepository(BaseRepository):
    model = TasksORM
    mapper = TaskDataMapper
