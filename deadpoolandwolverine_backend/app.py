from fastapi import FastAPI

from deadpoolandwolverine_backend.routers import exemple

app = FastAPI()

app.include_router(exemple.router)
