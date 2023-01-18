from fastapi import FastAPI
from api_backend.api import app_router
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*"
]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["POST", "PUT", "GET", "DELETE"],
    allow_headers=["*"]
)

app.include_router(app_router)
