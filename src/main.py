from config import get_settings
from fastapi import FastAPI
from applicants.routers import applicants_router
from companies.routers import company_router, vacancy_router

settings = get_settings()


app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG
)

app.include_router(applicants_router)
app.include_router(company_router)
app.include_router(vacancy_router)

