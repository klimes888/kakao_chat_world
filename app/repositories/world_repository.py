import logging
from datetime import datetime
from app.dto.world_dto import WorldDto
from app.extensions import db
from app.models.content_model import World
from sqlalchemy.orm import joinedload

from app.models.user_model import Assignment

logger = logging.getLogger(__name__)


class WorldRepository:
    @staticmethod
    def add_world(world: WorldDto):
        world_dict = world.to_dict()
        new_item = World(**world_dict)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    def query_world_with_user(bot_id: str):
        world = (
            db.session.query(World)
            .options(
                joinedload(World.assignment).joinedload(Assignment.user),
                joinedload(World.content),
            )
            .filter(World.bot_id == bot_id)
            .first()
        )

        return world

    def query_world_by_name(world: WorldDto):
        result = db.session.query(World).filter_by(name=world.name).first()
        return result
