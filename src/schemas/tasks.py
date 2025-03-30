from datetime import datetime

from pydantic import BaseModel


class TaskAddRequest(BaseModel):
    title: str
    description: str
    created_at: datetime
    updated_at: datetime


class Task(TaskAddRequest):
    id: int
