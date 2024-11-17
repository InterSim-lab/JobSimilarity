from pydantic_settings import BaseSettings
from pathlib import Path

from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    PROJECT_NAME: str = "Job Recommendation API"
    
    DATA_DIR: Path = Path("data")
    EMBEDDINGS_FILE: str = "embeddings.h5"
    DATASET_FILE: str = "dataset.csv"
    
    class Config:
        case_sensitive = True

settings = Settings()