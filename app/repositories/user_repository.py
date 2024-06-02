import logging
from datetime import datetime
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
        logger.info(f" ---> user_dict: {user_dict}")
        new_item = User(**user_dict)
        logger.info(f" ---> new_item: {new_item}")

        db.session.add(new_item)
        db.session.flush()
        return new_item

    @staticmethod
    def add_assignment(user: UserDto, world: WorldDto, assignment: AssignmentDto):
        new_item = Assignment(user_id=user.id, world_id=world.id, assignment=assignment)
        db.session.add(new_item)
        db.session.commit()
        return new_item
