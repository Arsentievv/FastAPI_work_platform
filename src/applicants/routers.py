from fastapi import APIRouter, Depends
from applicants.crud.resumes_crud import ResumesCRUD
from applicants.crud.workers_crud import WorkerCRUD
from applicants.schemas import worker_schemas, resume_schemas, experience_schemas, education_schemas
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session


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
    return await worker


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
    return await worker


@applicants_router.get(
    "/{worker_id}",
    response_model=worker_schemas.WorkerGetWithResumes,
    description="get worker by ID",
    status_code=200
)
async def get_worker_by_id_with_resumes(
        worker_id: int,
        db: AsyncSession = Depends(get_session)
):
    worker = WorkerCRUD.get_worker_by_id(db=db, worker_id=worker_id)
    return await worker


@applicants_router.post(
    "/create_resume",
    response_model=resume_schemas.ResumeGet,
    description="Create resume",
    status_code=201
)
async def create_resume(
        resume: resume_schemas.ResumeCreate,
        db: AsyncSession = Depends(get_session)
):
    resume = ResumesCRUD.create_resume(db=db, resume=resume)
    return await resume


@applicants_router.get(
    "/resumes/id/{resume_id}",
    response_model=resume_schemas.ResumeWithConnections,
    description="Get resume with education and work experience",
    status_code=200
)
async def get_resume_by_id(resume_id: int, db: AsyncSession = Depends(get_session)):
    resume = ResumesCRUD.get_resume_by_id(db=db, resume_id=resume_id)
    return await resume


@applicants_router.get(
    "/resumes/title/{resumes_title}",
    response_model=list[resume_schemas.ResumeGet],
    description="Get all resumes by title",
    status_code=200
)
async def get_resumes_by_title(resume_title: str, db: AsyncSession = Depends(get_session)):
    resumes = ResumesCRUD.get_resumes_by_title(db=db, resume_title=resume_title)
    return await resumes


@applicants_router.get(
    "/{worker_id}/resumes/all",
    response_model=list[resume_schemas.ResumeGet],
    description="Get all applicant's resumes",
    status_code=200
)
async def get_all_workers_resumes(worker_id: int, db: AsyncSession = Depends(get_session)):
    resumes = ResumesCRUD.get_all_workers_resume(db=db, worker_id=worker_id)
    return await resumes


@applicants_router.post(
    "/education/add",
    response_model=education_schemas.EducationGet,
    description="Create resumes education information",
    status_code=201
)
async def create_education_for_resume(
        education: education_schemas.EducationCreate,
        db: AsyncSession = Depends(get_session)
):
    education = ResumesCRUD.create_education(education=education, db=db)
    return await education


@applicants_router.post(
    "/experience/add",
    response_model=experience_schemas.ExperienceGet,
    description="Create resumes experience information",
    status_code=201
)
async def create_experience_for_resume(
        experience: experience_schemas.ExperienceCreate,
        db: AsyncSession = Depends(get_session)
):
    education = ResumesCRUD.create_experience(experience=experience, db=db)
    return await education

