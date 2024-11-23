import h5py
import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict
from app.config import settings

class JobAction:
    def __init__(self):
        self._loader()
    
    def _loader(self):
        """
        Loads the dataset and embeddings from disk.

        This method is called in the constructor and is not intended to be called
        directly.

        The dataset is loaded into a pandas dataframe. The embeddings are loaded
        into a numpy array.

        The dataframe is modified in place to add an "id" column with the index
        of each row.

        The embeddings are not modified.
        """
        self.df = pd.read_csv(settings.DATA_DIR / settings.DATASET_FILE)
        self.df.fillna("", inplace=True)
        self.df["id"] = self.df.index

        with h5py.File(settings.DATA_DIR / settings.EMBEDDINGS_FILE, "r") as f:
            self.embeddings = np.array(f["embeddings"])

    def get_random_jobs(self, limit: int = 10) -> List[Dict]:
        """
        Returns a list of random jobs.

        Args:
            limit (int): The number of random jobs to return. Defaults to 10.

        Returns:
            List[Dict]: A list of jobs, each represented as a dictionary.
        """
        return self.df.sample(limit).to_dict("records")
    
    def get_jobs_by_category(self, category: str, limit: int = 10) -> List[Dict]:
        """
        Returns a list of jobs that belong to the given category.

        Args:
            category (str): The category of jobs to return.
            limit (int): The number of jobs to return. Defaults to 10.

        Returns:
            List[Dict]: A list of jobs, each represented as a dictionary.
        """
        return self.df[self.df["category"] == category].sample(limit).to_dict("records")

    def get_job_detail(self, id: int) -> Dict:
        """
        Returns the details of a job.

        Args:
            id (int): The ID of the job to return.

        Returns:
            Dict: The details of the job, represented as a dictionary.
        """ 
        return self.df.iloc[id].to_dict()
    
    def get_similar_jobs(self, id: int, limit: int = 10) -> List[Dict]:
        """
        Returns a list of jobs that are similar to the job with the given ID.

        Similarity is determined by the cosine similarity of the embeddings of
        the job descriptions.

        Args:
            id (int): The ID of the job to find similar jobs for.
            limit (int): The number of similar jobs to return. Defaults to 10.

        Returns:
            List[Dict]: A list of similar jobs, each represented as a dictionary.
        """

        similarities = cosine_similarity([self.embeddings[id]], self.embeddings)[0]
        similar_indices = np.argsort(similarities)[::-1][1:limit + 1]
        similar_jobs = self.df.iloc[similar_indices].copy()

        similar_jobs["similarity_score"] = similarities[similar_indices]

        return similar_jobs.to_dict("records")

    def get_find_jobs_by_title(self, title: str) -> List[Dict]:
        """
        Returns a list of jobs that contain the given title.

        Args:
            title (str): The title of the jobs to return.
            limit (int): The number of jobs to return. Defaults to 10.

        Returns:
            List[Dict]: A list of jobs, each represented as a dictionary.
        """
        return self.df[self.df["title"].str.contains(title)].to_dict("records")