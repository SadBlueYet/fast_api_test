from sqlalchemy import select

from database import new_session, TaskOrm
from schemas import SCreateTask, SGetTask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: SCreateTask) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def get_all(cls) -> list[SGetTask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [SGetTask.model_validate(task_model) for task_model in task_models]
            return task_schemas