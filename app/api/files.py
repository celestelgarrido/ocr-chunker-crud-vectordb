from fastapi import APIRouter
from app.services.ocr import extract_text
from app.services.chunking import chunking_text

files = APIRouter()

@files.get("/files/upload")
def upload_files():
    extract_text()
    chunks = chunking_text()
    # The main idea is that version 2 will use this chunks to create embedding and save in Pinecone


