import logging
from datetime import datetime
from app.extensions import db
from app.dto.user_dto import UserDto
from app.models.user_model import User

logger = logging.getLogger(__name__)


class UserRepository:
    @staticmethod
    def add_user(user: UserDto):
        user_dict = user.to_dict()
        new_item = User(**user_dict)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def get_user_by_chat_id(name):
        return User.query.filter_by(name=name).first()
