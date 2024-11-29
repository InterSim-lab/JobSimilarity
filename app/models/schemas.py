from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):
    id: int
    title: str
    company: str
    category: str
    status: Optional[str] = None
    min_edu: Optional[str] = None
    min_exp: Optional[str] = None
    description: str
    urlJob: str
    urlImg: str

class JobSimilarity(BaseModel):
    title: str
    company: str
    category: str
    status: Optional[str] = None
    min_edu: Optional[str] = None
    min_exp: Optional[str] = None
    description: str
    urlJob: str
    urlImg: str
    similarity_score: float

class IntersimQ(BaseModel):
    name: str
    institution: str
    degree: str
    describe_me: Optional[str] = None

    title: str
    company: str
    job_description: str