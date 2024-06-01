from pydantic import BaseModel
from app.extensions import db
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    SmallInteger,
    String,
    DateTime,
    ForeignKey,
    JSON,
)


# 콘텐츠 월드 (각 톡방 마다 하나씩 존재)
class World(db.Model):
    __tablename__ = "world"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bot_id = Column(String(120), unique=True, nullable=False)
    name = Column(String(40), nullable=False)  # world 이름
    desc = Column(String(300), nullable=False)  # world 설명
    image_url = Column(String(120))  # 콘텐츠 대표 썸네일
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    update_at = Column(DateTime)
    remove_at = Column(DateTime)
    content = relationship("Content", back_populates="world")
    assignment = relationship("Assignment", back_populates="world", uselist=False)

    def __repr__(self):
        return f"<World(name={self.name}, chat_id={self.id})>"


# 콘텐츠 모델 (국가)
class Content(db.Model):
    __tablename__ = "content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    world_id = Column(Integer, ForeignKey("world.id"), nullable=False)
    name = Column(String(40), nullable=False)  # 콘텐츠 이름
    desc = Column(String(300), nullable=False)  # 콘텐츠 설명
    image_url = Column(String(120), nullable=False)  # 콘텐츠 대표 썸네일
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    update_at = Column(DateTime)
    remove_at = Column(DateTime)
    world = relationship("World", back_populates="subContent")
    sub_content = relationship("SubContent", back_populates="content")
    assignment = relationship("Assignment", back_populates="content")

    def __repr__(self):
        return f"<Content(name={self.name}, chat_id={self.id})>"


# 콘텐츠 하위 테이블
class SubContent(db.Model):
    __tablename__ = "sub_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content_id = Column(Integer, ForeignKey("content.id"), nullable=False)
    desc = Column(String(150), nullable=False)  # 콘텐츠 설명
    name = Column(String(40), nullable=False)  # 콘텐츠 이름
    type = Column(SmallInteger, nullable=False)  #  타입 SubContentType 참고
    value = Column(JSON, nullable=False)
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    update_at = Column(DateTime)
    remove_at = Column(DateTime)
    content = relationship("Content", back_populates="sub_content")
    assignment = relationship("Assignment", back_populates="sub_content")
    force_defense = relationship("ForceDefense", back_populates="sub_content")

    def __repr__(self):
        return f"<SubContent(name={self.name}, chat_id={self.id})>"


class Status(db.Model):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(20), nullable=False)  # 상태 유형 (예: 재정, 국방)
    data = Column(JSON, nullable=False)  # 상태 데이터 (JSON 형식)

    def __repr__(self):
        return f"<Status(type={self.type}, state_id={self.id})>"


# 해당 콘텐츠에서 역할
class Assignment(db.Model):
    __tablename__ = "assignment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    world_id = Column(Integer, ForeignKey("world.id"))
    content_id = Column(Integer, ForeignKey("content.id"))
    sub_content_id = Column(Integer, ForeignKey("sub_content.id"))
    role = Column(String(50), nullable=False)  # UserRole enum 참고
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    update_at = Column(DateTime)
    remove_at = Column(DateTime)
    user = relationship("User", back_populates="assignment")
    world = relationship("World", back_populates="assignment")
    content = relationship("Content", back_populates="assignment")
    sub_content = relationship("SubContent", back_populates="assignment")

    def __repr__(self):
        return f"<Assignment(user_id={self.user_id}, organization_id={self.sub_content_id}, role={self.role})>"


# 국방
class ForceDefense(db.Model):
    __tablename__ = "force_defense"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sub_content_id = Column(Integer, ForeignKey("sub_content.id"), nullable=False)
    desc = Column(String(300), nullable=False)  # 콘텐츠 설명
    type = Column(SmallInteger, nullable=False)  #  타입 ForceDefenseType 참고
    count = Column(String(12), nullable=False)  # 병력 수
    value = Column(JSON, nullable=False)
    update_at = Column(DateTime)
    sub_content = relationship("SubContent", back_populates="force_defense")

    def __repr__(self):
        return f"<ForceDefense(name={self.type}, value={self.value})>"


# 무기 장비
class Weapon(db.Model):
    __tablename__ = "weapon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)  # 무기 이름
    desc = Column(String(300), nullable=False)  # 무기 설명
    image_url = Column(String(120), nullable=False)  # 무기 대표 썸네일
    count = Column(String(12), nullable=False)  # 무기 수
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    update_at = Column(DateTime)
    remove_at = Column(DateTime)

    def __repr__(self):
        return f"<Weapon(name={self.name}, chat_id={self.id})>"


# 운영에서 관리하는 무기 리스트 (무기 장비와 다대다)
class WeaponList(db.Model):
    __tablename__ = "weapon_list"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)  # 무기 이름
    desc = Column(String(300), nullable=False)  # 무기 설명
    weapon_type = Column(String(40), nullable=False)  # 무기 타입
    weapon_weight = Column(SmallInteger, nullable=False)  # 무기 무게 (경, 중, 일반, 중)
    generation = Column(String(4), nullable=False)  # 무기 세대

    def __repr__(self):
        return f"<WeaponList(name={self.name}, chat_id={self.id})>"


class ContentDto(BaseModel):
    name: str
    chat_id: str
