from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    ARCHIVED = "archived"


class ProjectAddRequest(BaseModel):
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime


class Project(ProjectAddRequest):
    id: int


class TaskWithStatus(BaseModel):
    id: int
    title: str
    description: str | None
    status: TaskStatus
    created_at: datetime
    updated_at: datetime
    project_id: int | None


class ProjectStats(BaseModel):
    project_id: int
    project_name: str
    total_tasks: int
    todo_tasks: int
    in_progress_tasks: int
    done_tasks: int
