from fastapi import APIRouter, UploadFile, File
from app.services.file_handler import extract_text_from_pdf
import os

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    file_path = f"temp/{file.filename}"
    os.makedirs("temp", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(contents)
    extracted_text = extract_text_from_pdf(file_path)
    return {"filename": file.filename, "preview": extracted_text[:1000]}
