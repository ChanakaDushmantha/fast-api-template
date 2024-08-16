import logging
import time

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from api import all_routers
from config.logger import setup_logger
from db.models import models
from db.session import engine
from exception.exception_handler import add_exception_handler

logger = logging.getLogger(__name__)
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


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    cpu_start_time = time.process_time()
    response = await call_next(request)
    process_time = time.time() - start_time
    cpu_time = time.process_time() - cpu_start_time
    logger.info(f"Path: {request.url.path}, Process time: {process_time} seconds, CPU time: {cpu_time} seconds")
    return response


app.include_router(all_routers)
add_exception_handler(app)
models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
