import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.software.routers import platform, software, tag, license
from api.software.data.database import engine, Base

app = FastAPI()

# Initialize the database
Base.metadata.create_all(bind=engine)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Include the routers for each model
app.include_router(platform.router, prefix="/platforms", tags=["platforms"])
app.include_router(software.router, prefix="/software", tags=["software"])
app.include_router(tag.router, prefix="/tags", tags=["tags"])
app.include_router(license.router, prefix="/licenses", tags=["licenses"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
