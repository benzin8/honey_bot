from sqlalchemy import Column, Integer, String, Float, Text, BigInteger
from backend.models.base import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    phone = Column(String(12))

    def __repr__(self):
        return f"<User(name={self.name}, telegram_id={self.telegram_id})>"