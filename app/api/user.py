import logging

from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED

from db.session import db_dependency
from models.response import GenericResponse
from models.user import UserModelIn
from service.user import create_user

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/v1/user",
    tags=["User"]
)


@router.post("/", status_code=HTTP_201_CREATED, response_model=GenericResponse)
async def create(user: UserModelIn, db: db_dependency):
    logger.debug(f'Request for create data: {user}')
    user_response = await create_user(user, db)

    return GenericResponse(success=True, message="User created successfully", data=user_response)
