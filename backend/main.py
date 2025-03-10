import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, students, attendance, devices
from app.core.config import settings
from app.db.database import engine
from app.db.models import Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Attendance System API",
    description="Facial recognition based attendance system API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(students.router, prefix="/api/students", tags=["Students"])
app.include_router(attendance.router, prefix="/api/attendance", tags=["Attendance"])
app.include_router(devices.router, prefix="/api/devices", tags=["Devices"])

@app.get("/")
async def root():
    return {"message": "Welcome to Smart Attendance System API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
