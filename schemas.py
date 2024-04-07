from typing import Optional
from pydantic import BaseModel


class SCreateTask(BaseModel):
    name: str
    description: Optional[str] = None


class SGetTask(SCreateTask):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int