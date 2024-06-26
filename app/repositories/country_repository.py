import logging
from datetime import datetime
from app.dto.country_dto import CountryDto
from app.dto.country_dto import CountryDto
from app.extensions import db
from app.models.content_model import Content, World
from sqlalchemy.orm import joinedload
from app.models.user_model import Assignment

logger = logging.getLogger(__name__)


class CountryRepository:
    @staticmethod
    def add_country(country: CountryDto):
        country_dict = country.to_dict()
        new_item = Content(**country_dict)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    def query_country_by_name(country: CountryDto):
        result = (
            db.session.query(Content)
            .options(joinedload(Content.world))
            .filter_by(name=country.name)
            .first()
        )
        return result
