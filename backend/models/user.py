import uuid

from sqlalchemy import Column, String, Boolean
from backend.db.connection import Base

class User(Base):
    __tablename__ = "users"

    # id = Column(Integer, primary_key=True, index=True)
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return (
            f"<User(id={self.id}, username={self.username}, "
            f"email={self.email}, active={self.is_active}, admin={self.is_admin})>"
        )
