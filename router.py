from typing import Annotated
from fastapi import Depends
from fastapi import APIRouter

from repository import TaskRepository
from schemas import SCreateTask, SGetTask, STaskId


router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

@router.post("")
async def add_task(
    task: Annotated[SCreateTask, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[SGetTask]: 
    tasks = await TaskRepository.get_all()
    return tasks