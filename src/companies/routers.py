from fastapi import APIRouter, Depends, Query, Body, Path
from companies.schemas import company_schemas, vacancy_schemas
from companies.crud.company_crud import CompanyCRUD
from companies.crud.vacancies_crud import VacanciesCRUD
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from utils.enums import Workload


company_router = APIRouter()
vacancy_router = APIRouter()


@company_router.post(
    "/create",
    response_model=company_schemas.CompanyGet,
    status_code=201,
    description="Create company"
)
async def create_company(
        company: company_schemas.CompanyCreate,
        db: AsyncSession = Depends(get_session)
):
    result = CompanyCRUD.create_company(
        db=db,
        company=company
    )
    return await result


@company_router.get(
    "/company/{company_id}",
    response_model=company_schemas.CompanyGet,
    status_code=200,
    description="Get company by ID"
)
async def get_company_by_id(
        company_id: int,
        db: AsyncSession = Depends(get_session)
):
    result = CompanyCRUD.get_company_by_id(db=db, company_id=company_id)
    return await result


@company_router.get(
    "/company/name/{company_name}",
    response_model=list[company_schemas.CompanyGet],
    status_code=200,
    description="Get company by name"
)
async def get_company_by_name(
        company_title: str,
        db: AsyncSession = Depends(get_session)
):
    result = CompanyCRUD.get_company_by_title(db=db, company_title=company_title)
    return await result


@company_router.get(
    "/company/{company_id}/vacancies",
    response_model=list[vacancy_schemas.VacancyGet],
    status_code=200,
    description="Get company vacancies"
)
async def get_company_vacancies(
        company_id: int,
        db: AsyncSession = Depends(get_session)
):
    result = CompanyCRUD.get_company_vacancies(db=db, company_id=company_id)
    return await result


@vacancy_router.post(
    "/company/create_vacancy",
    response_model=vacancy_schemas.VacancyBase,
    status_code=201,
    description="Create vacancy"
)
async def create_vacancy(
        vacancy: vacancy_schemas.VacancyCreate,
        db: AsyncSession = Depends(get_session)
):
    result = VacanciesCRUD.create_vacancy(vacancy=vacancy, db=db)
    return await result


@vacancy_router.get(
    "/vacancy/{id}",
    response_model=vacancy_schemas.VacancyGet,
    status_code=200,
    description="Get vacancy by ID"
)
async def get_vacancy_by_id(
        vacancy_id: int,
        db: AsyncSession = Depends(get_session)
):
    result = VacanciesCRUD.get_vacancy_by_id(vacancy_id=vacancy_id, db=db)
    return await result


@vacancy_router.get(
    "/vacancy/name/{vacancy_name}",
    response_model=list[vacancy_schemas.VacancyGet],
    status_code=200,
    description="Get vacancies by name"
)
async def get_vacancies_by_name(
        vacancy_title: str,
        db: AsyncSession = Depends(get_session)
):
    result = VacanciesCRUD.get_vacancies_by_name(vacancy_title=vacancy_title, db=db)
    return await result


@vacancy_router.get(
    "/find_vacancy",
    response_model=list[vacancy_schemas.VacancyGet],
    status_code=200,
    description="Get filtered vacancies"
)
async def get_filtered_vacancies(
        workload: Workload,
        vacancy_title: str | None = Query(None),
        compensation: float | None = Query(None),
        db: AsyncSession = Depends(get_session)
):
    result = VacanciesCRUD.get_vacancy_by_filters(
        vacancy_title=vacancy_title,
        compensation=compensation,
        workload=workload,
        db=db
    )
    return await result
