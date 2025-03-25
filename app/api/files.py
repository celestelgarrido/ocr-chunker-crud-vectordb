from fastapi import APIRouter
from app.services.ocr import extract_text
from app.services.chunking import chunking_text

files = APIRouter()

@files.get("/files/upload")
def upload_files():
    #extract_text()
    chunking_text()


