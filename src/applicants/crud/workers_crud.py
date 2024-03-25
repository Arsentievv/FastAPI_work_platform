from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from applicants.models import Worker, Resume
from applicants.schemas import worker_schemas


class WorkerCRUD:

    @staticmethod
    async def create_worker(db: AsyncSession, worker: worker_schemas.WorkerCreate):
        worker_db = Worker(
            first_name=worker.first_name,
            last_name=worker.last_name,
            date_of_birth=worker.date_of_birth
        )
        db.add(worker_db)
        await db.commit()
        return worker_db

    @staticmethod
    async def get_worker_by_id(db: AsyncSession, worker_id: int):
        result = await db.execute(select(Worker).filter(Worker.id == worker_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_worker_by_resume_id(db: AsyncSession, resume_id: int):
        resume = await db.execute(select(Resume).filter(Resume.id == resume_id))
        resume = resume.first()
        worker_id = resume.worker_id
        result = await db.execute(select(Worker).filter(Worker.id == worker_id))
        return result.scalar_one_or_none()
