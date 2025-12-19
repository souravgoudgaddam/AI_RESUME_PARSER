from fastapi import FastAPI
from App.api import resume, match

app = FastAPI(title="AI Resume Parser")

app.include_router(resume.router)
app.include_router(match.router)
