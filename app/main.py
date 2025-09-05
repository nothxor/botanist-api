from fastapi import FastAPI
from app.api.plants import router as plants_router

app = FastAPI(
    title="Botanist API",
    description="Handler system for plant management",
    version="0.0.1"
)

@app.get("/")
async def root():
    return {"message": "Welcome to Botanist! 🌱"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "botanist-api"
    }

app.include_router(plants_router)