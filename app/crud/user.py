from logging import getLogger

from db.models.models import User

logger = getLogger(__name__)


async def save_user(user: User, db):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
