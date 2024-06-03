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
        user_data = UserDto(name="test1", chat_id=data["chat_id"])
        # user_data = UserDto(name="test1", chat_id="test2")

        user_result = UserRepository.add_user_flush(user_data)

        world_data = WorldDto(**data)

        world_result = WorldRepository.add_world(world_data)
        assignment_item = AssignmentDto(
            user_id=user_result.id,
            world_id=world_result.id,
            role=UserRole["ADMIN"].value,
        )
        UserRepository.add_assignment(assignment_item)

    def query_world(data: dict):
        world_data = WorldDto(**data)
        world = WorldRepository.query_world(world_data)
        return world
