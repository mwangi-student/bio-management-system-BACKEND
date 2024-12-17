from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, DateTime, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# connecting to the db
engine = create_engine('sqlite:///school.db', echo=True)

# create a session
session = sessionmaker(bind=engine)

# create an instance
def get_db():
    db = session()
    try:
        yield db

    finally:
        db.close()


# create base model
Base = declarative_base()

# create a model 
# must provide table name via the __tablename__attribute
# must have at least one columndefined.

class Students(Base):
    __tablename__= "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    phone = Column(VARCHAR(15), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)

class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_title = Column(String(255), nullable=False)
    instructor_id = Column(Integer, ForeignKey('instructors.id'))
    created_at = Column(DateTime, default=datetime.now)

class Instructors(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id  = Column(Integer, ForeignKey('courses.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    created_at = Column(DateTime, default=datetime.now)

class Photos(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'))
    instructor_id = Column(Integer, ForeignKey("instructors.id"))  
    course_id = Column(Integer, ForeignKey('courses.id'))
    created_at = Column(DateTime, default=datetime.now)

