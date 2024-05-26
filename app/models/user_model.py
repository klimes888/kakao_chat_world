from pydantic import BaseModel
from app.extensions import db
from datetime import datetime
from sqlalchemy import Column, Integer, SmallInteger, String, DateTime, ForeignKey, orm


# 유저 모델
class User:
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    chat_id = Column(String(100), nullable=False, unique=True)  # chatbot user id
    create_at = Column(DateTime, default=datetime, nullable=False)
    update_at = Column(DateTime, nullable=True)
    remove_at = Column(DateTime, nullable=True)
    role = orm.relationship("Role", back_populates="user", uselist=False)

    def __repr__(self):
        return f"<Message {self}>"


class Role:
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    role = Column(SmallInteger, nullable=False)  # UserRole enum 참고
    name = Column(String(40), nullable=False)  # 역할 이름
    create_at = Column(DateTime, default=datetime, nullable=False)

    def __repr__(self):
        return f"<Message {self}>"


class UserDto(BaseModel):
    name: str
    chat_id: str


class RoleDto(BaseModel):
    name: str
    role: int
