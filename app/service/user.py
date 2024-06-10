from logging import getLogger

from crud.user import save_user
from db.models.models import User
from models.user import UserModelIn, UserModelOut

logger = getLogger(__name__)


async def create_user(user_model: UserModelIn, db):
    logger.info("Create user process started")
    user = User(
        email=user_model.email,
        password=user_model.password
    )

    db_obj = await save_user(user, db)

    user_response = UserModelOut(
        id=db_obj.id,
        email=db_obj.email,
        password=db_obj.password
    )

    logger.info("Create user process end")
    return user_response
