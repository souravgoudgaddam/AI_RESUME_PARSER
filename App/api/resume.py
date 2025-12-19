from fastapi import APIRouter,UploadFile
import shutil,os
from App.services.pdf_loader import extract_resume_text
from App.services.resume_parser import parse_resume
router=APIRouter(prefix='/resume',tags=['Resume'])

@router.post('/upload')
async def upload_resume(file:UploadFile):
    path=f'Data/interim/{file.filename}'
    with open(path,'wb') as buffer:
        shutil.copyfileobj(file.file,buffer)
    text = extract_resume_text(path)
    structured = parse_resume(text)

    return structured