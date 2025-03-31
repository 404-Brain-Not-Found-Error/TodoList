from src.models.projects import TasksORM, ProjectORM
from src.repositories.mappers.base import DataMapper
from src.schemas.tasks import Task
from src.schemas.projects import Project


class TaskDataMapper(DataMapper):
    db_model = TasksORM
    schema = Task


class ProjectDataMapper(DataMapper):
    db_model = ProjectORM
    schema = Project
