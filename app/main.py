from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.models.schemas import Job, JobSimilarity, IntersimQ
from app.services.jobs import JobAction

import json
import uuid

q = """
[ {"id": "q1", "question": "Selamat pagi, Emily! Bagaimana perjalanan Anda ke sini hari ini?", "type": "opening"}, {"id": "q2", "question": "Apa yang membuat Anda tertarik untuk menjadi seorang pengajar?", "type": "opening"}, {"id": "q3", "question": "Dengan latar belakang Anda di Ilmu Komunikasi dari Universitas Indonesia, bagaimana Anda mengaitkan passion Anda dalam media dan broadcasting dengan pekerjaan ini?", "type": "background"}, {"id": "q4", "question": "Dalam menjalani pekerjaan ini, dibutuhkan kesabaran dan empati dalam menghadapi siswa yang memiliki kebutuhan khusus. Bagaimana Anda menghadapi situasi seperti itu?", "type": "background"}, {"id": "q5", "question": "Bagaimana Anda akan menggambar strategi pengajaran yang efektif untuk siswa yang mengalami keterlambatan bicara?", "type": "technical assessment"}, {"id": "q6", "question": "Bagaimana Anda akan mengatasi situasi jika siswa tidak dapat mengikuti pelajaran karena kesulitan berbicara?", "type": "technical assessment"}, {"id": "q7", "question": "Dalam mengajar, Anda akan bekerja sama dengan guru lain dan tim kependidikan. Bagaimana Anda menjaga komunikasi yang baik dengan tim?", "type": "behavioral & soft skills"}, {"id": "q8", "question": "Bagaimana Anda akan menangani konflik atau perbedaan pendapat dengan guru lain dalam tim?", "type": "behavioral & soft skills"}, {"id": "q9", "question": "Apa yang membuat Anda tertarik untuk bergabung dengan PT Sentral Kreatifitas Group (CikalFOu) dan apa yang Anda harapkan dari peran ini?", "type": "career discussion"}, {"id": "q10", "question": "Kapan Anda siap untuk memulai pekerjaan ini jika Anda diterima?", "type": "logistics & next steps"}, {"id": "closing", "statement": "Terima kasih atas waktu dan kesediaan Anda untuk berbicara dengan kami. Kami akan segera memberikan kabar dalam beberapa hari ke depan.", "type": "closing"} ]
"""
q_example = json.loads(q)


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
    

@app.get("/api/generate/q")
async def generate_q():
    try:
        return {
            "id": uuid.uuid4(),
            "question": q_example
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))