from src.exceptions import ObjectNotFoundException, TaskNotFoundException
from src.schemas.tasks import TaskAddRequest, Task
from src.services.base import BaseService


class TaskService(BaseService):
    async def get_all(self):
        return await self.db.tasks.get_all()

    async def get_task(self, task_id: int):
        try:
            return await self.db.tasks.get_one(id=task_id)
        except ObjectNotFoundException as ex:
            raise TaskNotFoundException from ex

    async def add_task(self, task_data: TaskAddRequest):
        task: Task = await self.db.tasks.add(task_data)
        await self.db.commit()
        return task

    async def update_task(self, task_id: int, task_data: TaskAddRequest):
        try:
            await self.db.tasks.edit(id=task_id, data=task_data)
        except ObjectNotFoundException as ex:
            raise TaskNotFoundException from ex
        await self.db.commit()

    async def delete_task(self, task_id: int):
        await self.db.tasks.delete(id=task_id)
        await self.db.commit()