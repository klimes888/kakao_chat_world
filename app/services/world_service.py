import logging
from app.dto.world_dto import WorldDto
from app.repositories.user_repository import UserRepository
from app.repositories.world_repository import WorldRepository

logger = logging.getLogger(__name__)


class WorldService:
    @staticmethod
    def add_world(data: dict):

        world_data = WorldDto(**data)
        world = WorldRepository.add_world(world_data)
        return world
