from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from companies.models import Vacancy
from companies.schemas import vacancy_schemas
from utils.enums import Workload


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
    async def get_vacancies_by_name(db: AsyncSession, vacancy_title: str):
        result = await db.execute(select(Vacancy).filter(Vacancy.title.contains(vacancy_title)))
        return result.scalars().all()

    @staticmethod
    async def get_vacancy_by_filters(
            db: AsyncSession,
            vacancy_title: str | None,
            compensation: float | None,
            workload: Workload
    ):
        if vacancy_title and compensation:
            query = select(Vacancy).filter(and_(
                Vacancy.title.contains(vacancy_title),
                Vacancy.compensation == compensation,
                Vacancy.work_load == workload
            ))
        elif vacancy_title is not None and compensation is None:
            query = select(Vacancy).filter(
                Vacancy.title.contains(vacancy_title),
                Vacancy.work_load == workload
            )
        elif vacancy_title is None and compensation:
            query = select(Vacancy).filter(
                Vacancy.compensation == compensation,
                Vacancy.work_load == workload
            )
        else:
            query = select(Vacancy).filter(
                Vacancy.work_load == workload
            )
        result = await db.execute(query)
        return result.scalars().all()

