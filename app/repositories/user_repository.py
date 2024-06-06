import logging
from datetime import datetime

from sqlalchemy import or_
from app.dto.assignment_dto import AssignmentDto
from app.dto.world_dto import WorldDto
from app.extensions import db
from app.dto.user_dto import UserDto
from app.models.user_model import Assignment, User

logger = logging.getLogger(__name__)


class UserRepository:
    @staticmethod
    def add_user_commit(user: UserDto):
        user_dict = user.to_dict()
        new_item = User(**user_dict)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def add_user_flush(user: UserDto):
        user_dict = user.to_dict()
        new_item = User(**user_dict)
        db.session.add(new_item)
        db.session.flush()
        return new_item

    @staticmethod
    def add_assignment(assignment: AssignmentDto):
        assignment_data = assignment.to_dict()
        new_item = Assignment(**assignment_data)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def query_user_by_name(user: UserDto):
        result = (
            db.session.query(User)
            .filter(or_(User.name == user.name, User.chat_id == user.chat_id))
            .first()
        )
        return result
