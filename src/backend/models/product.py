from sqlalchemy import Column, Integer, String, Float, Text
from backend.models.base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    photo_id = Column(String(200))
    quantity = Column(Integer, default=0)

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, quantity={self.quantity})>"