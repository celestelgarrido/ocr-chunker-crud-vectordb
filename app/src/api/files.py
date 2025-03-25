from fastapi import APIRouter
from app.src.services.ocr import extract_text

files = APIRouter()

@files.get("/files/upload")
def upload_files():
    return extract_text()


