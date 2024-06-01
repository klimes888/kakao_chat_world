import logging
from app.dto.world_dto import WorldDto
from app.repositories.user_repository import UserRepository

logger = logging.getLogger(__name__)


class WorldService:
    @staticmethod
    def add_world(data: dict):

        world_data = WorldDto(**data)
        logger.info(f"world_data: {world_data}")
        # user = UserRepository.add_user(user_data)
        # return user
