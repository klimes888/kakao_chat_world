import logging

# types
from app.dto.assignment_dto import AssignmentDto
from app.dto.user_dto import UserDto
from app.dto.world_dto import WorldDto
from app.dto.country_dto import CountryDto

# services
from app.services.user_service import UserService
from app.services.world_service import WorldService

# repositories
from app.repositories.user_repository import UserRepository
from app.repositories.country_repository import CountryRepository
from app.types.enums import UserRole

# utils
from app.utils.codes import get_code
from app.utils.custom_response import CustomResponse

logger = logging.getLogger(__name__)


class CountryService:
    @staticmethod
    def add_country(data):
        country_name = data["name"]
        # 세계 쿼리
        world = WorldService.query_world_by_bot(data)

        if world is None:
            code = get_code("0005")
            return CustomResponse.simpleText(code)

        # 국가 검증
        is_exist = CountryService.query_country(data)
        code = get_code("0004")
        if is_exist:
            return CustomResponse.simpleText(code)
        # 국가 주인 검증
        is_exist_user = UserService.query_country_owner(data)

        if is_exist_user:
            return CustomResponse.simpleText(code)

        user_data = UserDto(name=data["user"], chat_id=data["chat_id"])
        user_result = UserRepository.add_user_flush(user_data)

        data["world_id"] = world.id
        data["name"] = country_name
        country_data = CountryDto(**data)
        country_result = CountryRepository.add_country(country_data)

        assignment_item = AssignmentDto(
            user_id=user_result.id,
            content_id=country_result.id,
            role=UserRole["ADMIN"].value,
        )
        UserRepository.add_assignment(assignment_item)
        code = get_code("0006").format(
            country_data.name,
            user_data.name,
            country_data.desc,
            0,
            0,
        )
        return CustomResponse.text_with_img(code, country_data.image_url)

    def query_country(data: dict):
        country_data = CountryDto(**data)
        country = CountryRepository.query_country_by_name(country_data)
        return country
