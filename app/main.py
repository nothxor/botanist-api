from fastapi import FastAPI
from app.api.plants import router as plants_router

app = FastAPI(
    title="QR Botanist",
    description="QR code handler system for plant management",
    version="0.0.1"
)

@app.get("/")
async def root():
    return {"message": "Welcome to QR Botanist! 🌱"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "qr-botanist"
    }

app.include_router(plants_router)