from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, text, integer, VARCHAR, DateTime

# create base model
Base = declarative_base()

# create a model 
# must provide table name via the __tablename__attribute
# must have at least one columndefined.

class Student(Base):
    __tablename__= "students"

    id = Column(integer(), primary_key=True)
    name = Column(text(), nullable=False)
    email = Column(VARCHAR(), nullable=False, unique=True)
    age = Column(integer(), nullable=False)
    phone = Column(VARCHAR(), nullable=False, unique=True)
    created_at = Column(DateTime(), default=DateTime.now)

