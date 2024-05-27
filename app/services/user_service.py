import logging
from app.dto.user_dto import UserDto
from app.repositories.user_repository import UserRepository

logger = logging.getLogger(__name__)


class UserService:
    @staticmethod
    def add_user(data: dict):

        user_data = UserDto(**data)
        user = UserRepository.add_user(user_data)
        return user
        # if user:
        # raise ValueError("Item already exists")
        # return UserRepository.add_inventory_item(name, quantity)
