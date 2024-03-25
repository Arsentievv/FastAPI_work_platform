from pydantic import BaseModel, Field
from datetime import datetime
from companies.schemas.vacancy_schemas import VacancyGet


class CompanyBase(BaseModel):
    title: str = Field(
        max_length=256,
        description="Company's title"
    )
    information: str | None = Field(
        default=None,
        max_length=1024,
        description="Company's description"
    )


class CompanyCreate(CompanyBase):
    pass


class CompanyGet(CompanyBase):
    id: int
    created_at: datetime
    updated_at: datetime


class CompanyGetWithConnections(CompanyGet):
    vacancies: list["VacancyGet"]
