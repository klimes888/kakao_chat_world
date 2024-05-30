from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, SmallInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.extensions import db


# 유저 모델
class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    chat_id = Column(String(100), nullable=False, unique=True)  # chatbot user id
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    update_at = Column(DateTime, nullable=True)
    remove_at = Column(DateTime, nullable=True)
    assignments = relationship(
        "Assignment", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(name={self.name}, chat_id={self.chat_id})>"


# class Role(db.Model):
#     __tablename__ = "role"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
#     role = Column(SmallInteger, nullable=False)  # UserRole enum 참고
#     name = Column(String(40), nullable=False)  # 역할 이름
#     create_at = Column(DateTime, default=datetime, nullable=False)
#     role = relationship("User", back_populates="role", uselist=False)

#     def __repr__(self):
#         return f"<Role(name={self.name}, role={self.role})>"


class RoleDto(BaseModel):
    name: str
    role: int
