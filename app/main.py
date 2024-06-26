import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import all_routers
from config.logger import setup_logger
from db.models import models
from db.session import engine
from exception.exception_handler import add_exception_handler

setup_logger()
app = FastAPI(
    description='< Repository Description >',
    version="1.0",
    title='< Repository Title >'
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"]
)

app.include_router(all_routers)
add_exception_handler(app)
models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
