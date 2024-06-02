import logging
from datetime import datetime
from app.dto.world_dto import WorldDto
from app.extensions import db
from app.models.content_model import World

logger = logging.getLogger(__name__)


class WorldRepository:
    @staticmethod
    def add_world(world: WorldDto):
        world_dict = world.to_dict()
        new_item = World(**world_dict)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    def query_world(world: WorldDto):
        world_dict = world.to_dict()
        query_item = World(**world_dict)
        result = db.session.query(query_item).first()

        return result

    # @staticmethod
    # def get_user_by_chat_id(name):
    #     return User.query.filter_by(name=name).first()
