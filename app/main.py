from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.models.schemas import Job, JobSimilarity, IntersimQ
from app.services.jobs import JobAction
# from app.services.intersim_q import InterSimQ

app = FastAPI(
    title="Job Similarity API",
    description="API for finding similar jobs",
    version="1.0.0",
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

actions = JobAction()
# IntersimQAI = InterSimQ()

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
        raise HTTPException(status_code=500, detail=f"Category {category} not found")
    
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
    
@app.get("/api/jobs", response_model=List[Job])
async def get_find_jobs_by_title(title: str = Query(None, description="The title of the jobs to return.")):
    try:
        if title is None:
            raise HTTPException(status_code=400, detail="title is required")
        return actions.get_find_jobs_by_title(title)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @app.post("/api/intersim/q", response_model=str)
# async def get_questions(data: IntersimQ):
#     prompt = f"""
# ### Question: Generate a set of interview questions for a {data.title} position at {data.company}. The questions should be derived from the following job description and candidate requirements.
#     Job Description:
#     {data.job_description}
# ### Input: Nama: {data.name}
#     Asal Institusi: {data.institution}
#     Prodi: {data.degree}
# ### Answer:
# """
#     try:
#         return IntersimQAI.generator(prompt)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))