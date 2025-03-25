from fastapi import FastAPI
from app.api.files import files

app = FastAPI(title="Mi API con FastAPI")

# Include routers endpoints
app.include_router(files)

 