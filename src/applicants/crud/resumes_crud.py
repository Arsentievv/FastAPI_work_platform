from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from applicants.models import Resume
from applicants.schemas import resume_schemas


class ResumesCRUD:

    @staticmethod
    async def create_resume(db: AsyncSession, resume: resume_schemas.ResumeCreate):
        resume_db = Resume(
            title=resume.title,
            compensation=resume.compensation,
            workload=resume.workload,
            educations=resume.educations,
            experience=resume.experience,
            worker_id=resume.worker_id
        )
        db.add(resume_db)
        await db.commit()
        return resume_db

    @staticmethod
    async def get_resume_by_id(db: AsyncSession, resume_id: int):
        result = await db.execute(select(Resume).filter(Resume.id == resume_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_resumes_by_title(db: AsyncSession, resume_title: str):
        result = await db.execute(select(Resume).fulter(Resume.title == resume_title))
        if result:
            return result.all()

    @staticmethod
    async def get_all_workers_resume(db: AsyncSession, worker_id: int):
        result = await db.execute(select(Resume).filter(Resume.worker_id == worker_id))
        if result:
            return result.all()