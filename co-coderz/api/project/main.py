import uvicorn
from fastapi import FastAPI
from api.project.routers import project, build, user  # Import the user router
from api.project.data.database import engine, Base

app = FastAPI()

# Initialize the database
Base.metadata.create_all(bind=engine)

# Include the routers for each model
app.include_router(project.router, prefix="/projects", tags=["projects"])
app.include_router(build.router, prefix="/builds", tags=["builds"])
app.include_router(user.router, prefix="/users", tags=["users"])  # Include the user router

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
