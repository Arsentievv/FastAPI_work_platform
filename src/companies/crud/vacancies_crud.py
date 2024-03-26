from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from companies.models import Vacancy
from companies.schemas import vacancy_schemas


class VacanciesCRUD:

    @staticmethod
    async def create_vacancy(db: AsyncSession, vacancy: vacancy_schemas.VacancyCreate):
        vacancy_db = Vacancy(
            title=vacancy.title,
            description=vacancy.description,
            compensation=vacancy.compensation,
            work_load=vacancy.work_load,
            company_id=vacancy.company_id
        )
        db.add(vacancy_db)
        await db.commit()
        return vacancy_db

    @staticmethod
    async def get_vacancy_by_id(db: AsyncSession, vacancy_id: int):
        result = await db.execute(select(Vacancy).filter(Vacancy.id == vacancy_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_vacancy_by_name(db: AsyncSession, vacancy_title: str):
        result = await db.execute(select(Vacancy).filter(Vacancy.title == vacancy_title))
        return result.all()