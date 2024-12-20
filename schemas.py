from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schemas for Students
class CreateStudentSchema(BaseModel):
    name: str
    email: str
    age: int
    phone: str

class StudentResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    age: int
    phone: str
    created_at: datetime

    class Config:
        from_attributes = True  # Updated from 'orm_mode' to 'from_attributes'


# Schemas for Courses
class CreateCourseSchema(BaseModel):
    course_title: str
    instructor_id: int

class CourseResponseSchema(BaseModel):
    id: int
    course_title: str
    instructor_id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Updated from 'orm_mode' to 'from_attributes'


# Schemas for Instructors
class CreateInstructorSchema(BaseModel):
    name: str
    email: str

class InstructorResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True  # Updated from 'orm_mode' to 'from_attributes'

# Schemas for Photos
class CreatePhotoSchema(BaseModel):
    url: str
    student_id: Optional[int] = None
    instructor_id: Optional[int] = None
    course_id: Optional[int] = None

class PhotoResponseSchema(BaseModel):
    id: int
    url: str
    student_id: Optional[int]
    instructor_id: Optional[int]
    course_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True  # Updated from 'orm_mode' to 'from_attributes'


# updating schemas
class UpdateStudentSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    phone: Optional[str] = None

class UpdateCourseSchema(BaseModel):
    course_title: Optional[str] = None
    instructor_id: Optional[int] = None

class UpdateInstructorSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

