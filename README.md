# Python FastAPI Backend Example
App to process documents and create chunks. The main idea is that version 2 will contain embedding and storage in pinecone.

# Technologies
We will use
- Poetry as a package manager (https://python-poetry.org/)
- FastAPI as a framework to develop our back end application (https://fastapi.tiangolo.com/)
- Uvicorn as server to run the application on the laptop (https://www.uvicorn.org/)
- Docling as a main library to extract text from documents (https://docling-project.github.io/docling/)

# Run example
1. Clone this repo
2. Install in your laptop poetry
```bash
brew install poetry
```
3. Install project dependencies
```bash
poetry install
```
4. Run app
```bash
poetry run python -m uvicorn app.main:app --reload
```

# Explanation
You could see results in path: app/api/files/output