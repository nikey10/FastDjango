from pydantic import BaseModel

print("----- schemas.py")

class BookBase(BaseModel):
    title: str
    author: str
    price: float

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
