from fastapi import APIRouter, Depends
from companies.schemas import company_schemas, vacancy_schemas
from companies.crud.company_crud import CompanyCRUD
from companies.crud.vacancies_crud import VacanciesCRUD
from sqlalchemy.ext.asyncio import AsyncSession


