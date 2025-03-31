from sqlalchemy import func, select

from src.exceptions import ObjectNotFoundException, ProjectNotFoundException
from src.schemas.projects import ProjectAddRequest, ProjectStats
from src.services.base import BaseService
from src.models.projects import TaskStatus
from src.models.tasks import TasksORM


class ProjectService(BaseService):
    async def get_all_projects(self):
        return await self.db.projects.get_all()

    async def get_project(self, project_id: int):
        try:
            return await self.db.projects.get_one(id=project_id)
        except ObjectNotFoundException as ex:
            raise ProjectNotFoundException from ex

    async def add_project(self, project_data: ProjectAddRequest):
        project = await self.db.projects.add(project_data)
        await self.db.commit()
        return project

    async def update_project(self, project_id: int, project_data: ProjectAddRequest):
        try:
            await self.db.projects.edit(id=project_id, data=project_data)
        except ObjectNotFoundException as ex:
            raise ProjectNotFoundException from ex
        await self.db.commit()

    async def delete_project(self, project_id: int):
        await self.db.projects.delete(id=project_id)
        await self.db.commit()

    async def get_project_stats(self, project_id: int) -> ProjectStats:

        project = await self.db.projects.get_one(id=project_id)

        query = select(
            func.count(TasksORM.id).label("total_tasks"),
            func.sum(func.case((TasksORM.status == TaskStatus.TODO, 1), else_=0)).label("todo_tasks"),
            func.sum(func.case((TasksORM.status == TaskStatus.IN_PROGRESS, 1), else_=0)).label("in_progress_tasks"),
            func.sum(func.case((TasksORM.status == TaskStatus.DONE, 1), else_=0)).label("done_tasks")
        ).where(TasksORM.project_id == project_id)

        result = await self.db.session.execute(query)
        stats = result.fetchone()

        return ProjectStats(
            project_id=project.id,
            project_name=project.name,
            total_tasks=stats.total_tasks or 0,
            todo_tasks=stats.todo_tasks or 0,
            in_progress_tasks=stats.in_progress_tasks or 0,
            done_tasks=stats.done_tasks or 0
        )

    async def get_all_projects_stats(self):
        projects = await self.get_all_projects()
        return [await self.get_project_stats(project.id) for project in projects]
