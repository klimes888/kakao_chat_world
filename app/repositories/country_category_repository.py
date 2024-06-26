import logging
from datetime import datetime
from app.dto.country_dto import CountryDto
from app.dto.country_category_dto import CountryCategoryDto
from app.extensions import db
from app.models.content_model import SubContent
from sqlalchemy.orm import joinedload
from app.models.user_model import Assignment

logger = logging.getLogger(__name__)


class CountryCategoryRepository:
    @staticmethod
    def add_country_category_flush(countryCategory: CountryCategoryDto):
        country_dict = countryCategory.to_dict()
        new_item = SubContent(**country_dict)
        db.session.add(new_item)
        db.session.flush()
        return new_item

    # def query_country_by_name(country: CountryDto):
    #     result = (
    #         db.session.query(Content)
    #         .options(joinedload(Content.world))
    #         .filter_by(name=country.name)
    #         .first()
    #     )
    #     return result
