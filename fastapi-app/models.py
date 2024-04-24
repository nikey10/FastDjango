from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

print("----- models.py")

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    price = Column(Float)

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, price={self.price})>"
