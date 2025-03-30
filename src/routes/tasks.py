from fastapi import APIRouter

from src.exceptions import TaskNotFoundException, TaskNotFoundHTTPException
from src.routes.dependencies import DBDep
from src.schemas.tasks import TaskAddRequest
from src.services.tasks import TaskService

router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.get("", summary="Получение всех задач")
async def get_tasks(db: DBDep):
    tasks = await TaskService(db).get_all()
    return {"status": 200, "data": tasks}


@router.get("/{id}", summary="Получение задачи по id")
async def get_task(task_id: int, db: DBDep):
    try:
        task = await TaskService(db).get_task(task_id)
    except TaskNotFoundException:
        raise TaskNotFoundHTTPException
    return {"status": 200, "data": task}


@router.post("", summary="Создание задачи")
async def create_task(db: DBDep, task_data: TaskAddRequest):
    task = await TaskService(db).add_task(task_data)
    return {"status": 201, "data": task.id}


@router.put("/{task_id}", summary="Обновление задачи")
async def update_task(task_id: int, db: DBDep, task_data: TaskAddRequest):
    try:
        await TaskService(db).update_task(task_id, task_data)
    except TaskNotFoundException:
        raise TaskNotFoundHTTPException
    return {"status": 204}


@router.delete("/{task_id}")
async def delete_task(task_id: int, db: DBDep):
    await TaskService(db).delete_task(task_id)
    return {}
