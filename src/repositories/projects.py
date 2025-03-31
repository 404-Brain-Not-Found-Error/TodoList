from src.models.projects import ProjectORM
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ProjectDataMapper


class ProjectsRepository(BaseRepository):
    model = ProjectORM
    mapper = ProjectDataMapper
