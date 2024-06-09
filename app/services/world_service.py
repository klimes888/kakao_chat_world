import logging

# repositories
from app.repositories.user_repository import UserRepository
from app.repositories.world_repository import WorldRepository

# services
from app.services.user_service import UserService

# utils
from app.utils.codes import get_code
from app.utils.custom_response import CustomResponse

# types
from app.types.enums import UserRole
from app.dto.assignment_dto import AssignmentDto
from app.dto.user_dto import UserDto
from app.dto.world_dto import WorldDto

logger = logging.getLogger(__name__)


class WorldService:
    @staticmethod
    def add_world(data):
        # 세계 검증
        is_exist = WorldService.query_world(data)
        code = get_code("0001")
        if is_exist:
            return CustomResponse.simpleText(code)

        is_exist_user = UserService.query_user(data)

        if is_exist_user:
            return CustomResponse.simpleText(code)

        user_data = UserDto(name=data["user"], chat_id=data["chat_id"])
        user_result = UserRepository.add_user_flush(user_data)

        world_data = WorldDto(**data)
        world_result = WorldRepository.add_world(world_data)

        assignment_item = AssignmentDto(
            user_id=user_result.id,
            world_id=world_result.id,
            role=UserRole["ADMIN"].value,
        )
        UserRepository.add_assignment(assignment_item)

        code = get_code("0000").format(data["name"], user_data.name, world_data.desc)
        return CustomResponse.simpleText(code)

    @staticmethod
    def query_world_with_user(bot_id):
        world = WorldRepository.query_world_with_user(bot_id)
        logger.info(f"world content {world.content}")
        logger.info(f"world name {world.name}")

        code = get_code("0003").format(
            world.name,
            world.assignment[0].user.name,
            world.desc,
            len(world.content),
            0,
        )
        return CustomResponse.text_with_img(code, world.image_url)

    @staticmethod
    def query_world(data: dict):
        world_data = WorldDto(**data)
        world = WorldRepository.query_world_by_name(world_data)
        return world

    @staticmethod
    def query_world_by_bot(data: dict):
        world_data = WorldDto(**data)
        world = WorldRepository.query_world_by_bot(world_data)
        return world
