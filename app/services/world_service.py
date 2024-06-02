import logging
from app.dto.assignment_dto import AssignmentDto
from app.extensions import db
from app.dto.user_dto import UserDto
from app.dto.world_dto import WorldDto
from app.models.content_model import World
from app.models.user_model import Assignment, User
from app.repositories.user_repository import UserRepository
from app.repositories.world_repository import WorldRepository
from app.types.enums import UserRole
from app.utils.custom_response import CustomResponse

logger = logging.getLogger(__name__)
fail_output = [
    {
        "simpleText": {"text": "서버 에러가 발생했습니다"},
    }
]


class WorldService:
    @staticmethod
    def add_world(data):
        # user_data = UserDto(name=data["chat_id"], chat_id=data["chat_id"])

        # user_result = UserRepository.add_user_flush(user_data)

        # world_data = WorldDto(**data)

        # world_result = WorldRepository.add_world(world_data)
        # assignment_data = AssignmentDto(role=UserRole.ADMIN)
        # UserRepository.add_assignment(user_result, world_result, assignment_data)
        # try:
        #     user_data = UserDto(name=data["chat_id"], chat_id=data["chat_id"])
        #     user_result = UserRepository.add_user_flush(user_data)
        #     logger.info(f" ---> user_result: {user_result}")

        #     world_data = WorldDto(**data)
        #     world_result = WorldRepository.add_world(world_data)
        #     assignment_data = AssignmentDto(role=UserRole.ADMIN)
        #     UserRepository.add_assignment(user_result, world_result, assignment_data)

        #     # db.session.commit()
        # except Exception as e:
        #     db.session.rollback()
        #     return CustomResponse.simpleText("0001", fail_output)
        user_data = UserDto(name="test", chat_id=data["chat_id"])
        user_dict = user_data.to_dict()
        user_item = User(**user_dict)
        db.session.add(user_item)
        db.session.flush()

        world_data = WorldDto(**data)
        world_dict = world_data.to_dict()
        world_item = World(**world_dict)
        db.session.add(world_item)
        db.session.flush()

        assignment_item = AssignmentDto(
            user_id=user_item.id, world_id=world_item.id, role=UserRole["ADMIN"].value
        )

        assignment_data = assignment_item.to_dict()

        new_item = Assignment(**assignment_data)

        db.session.add(new_item)
        db.session.commit()

    def query_world(data: dict):

        world_data = WorldDto(**data)
        world = WorldRepository.query_world(world_data)
        return world
