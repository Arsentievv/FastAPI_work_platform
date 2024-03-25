from fastapi import APIRouter, Depends
from applicants.crud.resumes_crud import ResumesCRUD
from applicants.crud.workers_crud import WorkerCRUD
from applicants.schemas import worker_schemas
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession


applicants_router = APIRouter()


@applicants_router.post(
    "/create_applicant",
    response_model=worker_schemas.WorkerGet,
    description="Create applicant",
    status_code=201
)
async def create_applicant(
        applicant: worker_schemas.WorkerCreate,
        db: AsyncSession = Depends(get_session)
):
    worker = WorkerCRUD.create_worker(db=db, worker=applicant)
    return worker


@applicants_router.get(
    "/{worker_id}",
    response_model=worker_schemas.WorkerGet,
    description="get worker by ID",
    status_code=200
)
async def get_worker_by_id(
        worker_id: int,
        db: AsyncSession = Depends(get_session)
):
    worker = WorkerCRUD.get_worker_by_id(db=db, worker_id=worker_id)
    return worker


@applicants_router.get(
    "/{worker_id}/resumes",
    response_model=worker_schemas.WorkerGetWithResumes,
    description="get worker by ID",
    status_code=200
)
async def get_worker_by_id_with_resumes(
        worker_id: int,
        db: AsyncSession = Depends(get_session)
):
    worker = WorkerCRUD.get_worker_by_id(db=db, worker_id=worker_id)
    return worker
