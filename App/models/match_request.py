from pydantic import BaseModel
from App.models.resume_schema import Resume 
class MatchRequest(BaseModel):
    job_description: str
    resume: Resume
