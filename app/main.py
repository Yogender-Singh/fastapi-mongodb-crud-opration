import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api import router as api_router

app = FastAPI(
    title="MongoDB FastAPI Example",
    description="MongoDB CRUD operations with FastAPI",
    version="0.1.0",
)

app.include_router(api_router)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
