from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

print("----- database.py begin")

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)
print("----- database.py end")
