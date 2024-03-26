from sqlalchemy.ext.asyncio import AsyncSession
from companies.schemas import company_schemas
from companies.models import Company
from sqlalchemy import select


class CompanyCRUD:

    @staticmethod
    async def create_company(db: AsyncSession, company: company_schemas.CompanyCreate):
        db_company = Company(
            title=company.title,
            information=company.information
        )
        db.add(db_company)
        await db.commit()
        return db_company

    @staticmethod
    async def get_company_by_id(db: AsyncSession, company_id: int):
        result = await db.execute(select(Company).filter(Company.id == company_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_company_by_title(db: AsyncSession, company_title: str):
        result = await db.execute(select(Company).filter(Company.title.contains(company_title)))
        return result.scalars().all()

    @staticmethod
    async def get_company_vacancies(db: AsyncSession, company_id: int):
        query = await db.execute(select(Company).filter(Company.id == company_id))
        company = query.scalar_one_or_none()
        return company.vacancies







