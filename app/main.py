from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.models.schemas import Job, JobSimilarity
from app.services.jobs import JobAction

app = FastAPI(
    title="Job Similarity API",
    description="API for finding similar jobs",
    version="0.1.0",
    contact={
        "name": "Nangdosan",
        "url": "https://hapeace.vercel.app",
    })

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

actions = JobAction()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/api/jobs/random", response_model=List[Job])
async def get_random_jobs(limit: int = 10):
    try:
        return actions.get_random_jobs(limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/api/jobs/category/{category}", response_model=List[Job])
async def get_jobs_by_category(category: str, limit: int = 10):
    try:
        return actions.get_jobs_by_category(category, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/api/jobs/{id}", response_model=Job)
async def get_job_detail(id: int):
    try:
        return actions.get_job_detail(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/api/jobs/{id}/similar", response_model=List[JobSimilarity])
async def get_similar_jobs(id: int, limit: int = 10):
    try:
        return actions.get_similar_jobs(id, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))