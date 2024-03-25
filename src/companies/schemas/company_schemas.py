from pydantic import BaseModel
from datetime import datetime
from companies.schemas.vacancy_schemas import VacancyGet


class CompanyBase(BaseModel):
    title: str
    information: str


class CompanyCreate(CompanyBase):
    pass


class CompanyGet(CompanyBase):
    id: int
    created_at: datetime
    updated_at: datetime
    

class CompanyGetWithConnections(CompanyGet):
    vacancies: list["VacancyGet"]
