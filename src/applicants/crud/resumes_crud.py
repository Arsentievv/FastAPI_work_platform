from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from applicants.models import Resume, Education, Experience
from applicants.schemas import resume_schemas, education_schemas, experience_schemas


class ResumesCRUD:

    @staticmethod
    async def create_education(db: AsyncSession, education: education_schemas.EducationCreate):
        education_db = Education(
            organization_name=education.organization_name,
            speciality=education.speciality,
            grade=education.grade,
            date_of_start=education.date_of_start,
            date_of_finish=education.date_of_finish,
            resume_id=education.resume_id
        )
        db.add(education_db)
        await db.commit()
        return education_db

    @staticmethod
    async def create_experience(db: AsyncSession, experience: experience_schemas.ExperienceCreate):
        experience_db = Experience(
            company_title=experience.company_title,
            date_of_start=experience.date_of_start,
            date_of_finish=experience.date_of_finish,
            position=experience.position,
            description=experience.description,
            resume_id=experience.resume_id
        )
        db.add(experience_db)
        await db.commit()
        return experience_db

    @staticmethod
    async def create_resume(db: AsyncSession, resume: resume_schemas.ResumeCreate):
        resume_db = Resume(
            title=resume.title,
            compensation=resume.compensation,
            workload=resume.workload,
            worker_id=resume.worker_id
        )
        db.add(resume_db)
        await db.commit()
        education_list = []
        experiences_list = []
        for education in resume.educations:
            ed = Education(
                organization_name=education.organization_name,
                speciality=education.speciality,
                grade=education.grade,
                date_of_start=education.date_of_start,
                date_of_finish=education.date_of_finish,
                resume_id=resume_db.id
            )
            education_list.append(ed)
            db.add(ed)
        for experience in resume.experiences:
            ex = Experience(
                company_title=experience.company_title,
                date_of_start=experience.date_of_start,
                date_of_finish=experience.date_of_finish,
                position=experience.position,
                description=experience.description,
                resume_id=resume_db.id
            )
            db.add(ex)
            experiences_list.append(ex)
        await db.commit()
        return resume_db

    @staticmethod
    async def get_resume_by_id(db: AsyncSession, resume_id: int):
        query = (
            select(Resume)
            .options(joinedload(Resume.educations))
            .options(joinedload(Resume.experiences))
            .filter(Resume.id == resume_id)
        )
        result = await db.execute(query)
        return result.unique().scalar_one_or_none()

    @staticmethod
    async def get_resumes_by_title(db: AsyncSession, resume_title: str):
        result = await db.execute(select(Resume).filter(Resume.title == resume_title))
        return result.scalars().all()

    @staticmethod
    async def get_all_workers_resume(db: AsyncSession, worker_id: int):
        result = await db.execute(
            select(Resume)
            .options(joinedload(Resume.experiences))
            .options(joinedload(Resume.educations))
            .filter(Resume.worker_id == worker_id)
        )
        if result:
            return result.unique().scalars().all()
