from api.pipeline import router as pipeline_router

app.include_router(pipeline_router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to VoiceBridge AI",
        "version": settings.APP_VERSION,
        "status": "Running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }