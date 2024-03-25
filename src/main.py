from config import get_settings
from fastapi import FastAPI
from applicants.routers import applicants_router

settings = get_settings()


app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG
)

app.include_router(applicants_router)

