from fastapi import APIRouter

from src.exceptions import ProjectNotFoundHTTPException, ProjectNotFoundException
from src.routes.dependencies import DBDep
from src.schemas.projects import ProjectAddRequest
from src.services.projects import ProjectService

router = APIRouter(prefix="/projects", tags=["Проекты"])


@router.get("", summary="Получение всех проектов")
async def get_projects(db: DBDep):
    projects = await ProjectService(db).get_all_projects()
    return {"status": 200, "data": projects}


@router.get("/{project_id}", summary="Получение проекта по id")
async def get_project(project_id: int, db: DBDep):
    try:
        project = await ProjectService(db).get_project(project_id)
    except ProjectNotFoundException:
        raise ProjectNotFoundHTTPException
    return {"status": 200, "data": project}


@router.post("", summary="Создание проекта")
async def create_project(db: DBDep, project_data: ProjectAddRequest):
    project = await ProjectService(db).add_project(project_data)
    return {"status": 201, "data": project.id}


@router.put("/{project_id}", summary="Обновление проекта")
async def update_project(project_id: int, db: DBDep, project_data: ProjectAddRequest):
    try:
        await ProjectService(db).update_project(project_id, project_data)
    except ProjectNotFoundException:
        raise ProjectNotFoundHTTPException
    return {"status": 204}


@router.delete("/{project_id}", summary="Удаление проекта")
async def delete_project(project_id: int, db: DBDep):
    await ProjectService(db).delete_project(project_id)
    return {"status": 204}


@router.get("/{project_id}/stats", summary="Статистика по проекту")
async def get_project_stats(project_id: int, db: DBDep):
    try:
        stats = await ProjectService(db).get_project_stats(project_id)
    except ProjectNotFoundException:
        raise ProjectNotFoundHTTPException
    return {"status": 200, "data": stats}


@router.get("/stats/all", summary="Статистика по всем проектам")
async def get_all_projects_stats(db: DBDep):
    stats = await ProjectService(db).get_all_projects_stats()
    return {"status": 200, "data": stats}