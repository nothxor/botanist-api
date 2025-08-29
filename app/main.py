from fastapi import FastAPI

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

@app.get("/plants")
async def list_plants():
    return {
        "plants": {
            {
                "id": 1,
                "name": "Test Plant",
                "species": "Monstera deliciosa"
            },
            {
                "id": 2,
                "name": "Another Plant",
                "species": "Pothos aureus"
            }
        }
    }