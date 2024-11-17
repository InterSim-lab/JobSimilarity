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
    url: str

class JobSimilarity(BaseModel):
    title: str
    company: str
    category: str
    status: Optional[str] = None
    min_edu: Optional[str] = None
    min_exp: Optional[str] = None
    description: str
    url: str
    similarity_score: float