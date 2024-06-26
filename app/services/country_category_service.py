import logging

# types
from app.dto.assignment_dto import AssignmentDto
from app.dto.user_dto import UserDto
from app.dto.country_category_dto import CountryCategoryDto
from app.dto.country_dto import CountryDto

# services
from app.services.world_service import WorldService

# repositories
from app.repositories.country_category_repository import CountryCategoryRepository
from app.repositories.country_repository import CountryRepository
from app.types.enums import SubContentType

# utils
from app.utils.codes import get_code
from app.utils.custom_response import CustomResponse

logger = logging.getLogger(__name__)


# 국가 하위 인문, 국방, 경제 등
class CountryCategoryService:
    @staticmethod
    def add_country_category(country_id: int):
        list = [
            CountryCategoryDto(  # 경제
                type=SubContentType.ECONOMIC,
                country_id=country_id,
                name="",
                desc="",
                image_url="",
                value={"gdp": "0", "gni": "0", "rates": "0", "growth": "0"},
            ),
            CountryCategoryDto(  # 인문
                type=SubContentType.HUMANITY,
                country_id=country_id,
                name="",
                desc="",
                image_url="",
                value={
                    "population": "0",
                    "fertility": "0",
                },
            ),
            CountryCategoryDto(  # 군사 (병력 수)
                type=SubContentType.DEFENSE,
                country_id=country_id,
                name="",
                desc="",
                image_url="",
                value={"army": "0", "navy": "0", "air": "0", "marines": "0"},
            ),
        ]
        for item in list:
            CountryCategoryRepository.add_country_category_flush(item)

    def query_country(data: dict):
        country_data = CountryDto(**data)
        country = CountryRepository.query_country_by_name(country_data)
        return country
