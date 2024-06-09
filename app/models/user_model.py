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
    assignment = relationship(
        "Assignment", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(name={self.name}, chat_id={self.chat_id})>"


# 해당 콘텐츠에서 역할
class Assignment(db.Model):
    __tablename__ = "assignment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    world_id = Column(Integer, ForeignKey("world.id"))
    content_id = Column(Integer, ForeignKey("content.id"))
    sub_content_id = Column(Integer, ForeignKey("sub_content.id"))
    role = Column(SmallInteger, nullable=False)  # UserRole enum 참고
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    update_at = Column(DateTime)
    remove_at = Column(DateTime)
    user = relationship("User", back_populates="assignment")
    world = relationship("World", back_populates="assignment")
    content = relationship("Content", back_populates="assignment")
    sub_content = relationship("SubContent", back_populates="assignment")

    def __repr__(self):
        return f"<Assignment(user_id={self.user_id}, organization_id={self.sub_content_id}, role={self.role})>"
