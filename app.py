from fastapi import FastAPI, Depends, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import get_db, Students, Instructors, Courses, Photos
from schemas import CreateStudentSchema, UpdateStudentSchema, CreateInstructorSchema, UpdateInstructorSchema, CreateCourseSchema, UpdateCourseSchema

# Initialize FastAPI
app = FastAPI()


app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'])

@app.get("/")
def index():
    return {"message": "Welcome to MYO BIO MANAGEMENT SYSTEM"}

# ---------- Student Routes ----------

# Get all students
@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    students = db.query(Students).all()
    return students

# Get a single student by ID
@app.get("/students/{student_id}")
def get_single_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Students).filter(Students.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Create a new student
@app.post("/students")
def create_student(student: CreateStudentSchema, db: Session = Depends(get_db)):
    new_student = Students(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# Update an existing student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: UpdateStudentSchema, db: Session = Depends(get_db)):
    existing_student = db.query(Students).filter(Students.id == student_id).first()
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in student.dict(exclude_unset=True).items():
        setattr(existing_student, key, value)
    db.commit()
    db.refresh(existing_student)
    return existing_student

# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Students).filter(Students.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": f"Student {student_id} deleted successfully"}

# ---------- Instructor Routes ----------

# Get all instructors
@app.get("/instructors")
def get_instructors(db: Session = Depends(get_db)):
    instructors = db.query(Instructors).all()
    return instructors

# Get a single instructor by ID
@app.get("/instructors/{instructor_id}")
def get_single_instructor(instructor_id: int, db: Session = Depends(get_db)):
    instructor = db.query(Instructors).filter(Instructors.id == instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor

# Create a new instructor
@app.post("/instructors")
def create_instructor(instructor: CreateInstructorSchema, db: Session = Depends(get_db)):
    new_instructor = Instructors(**instructor.dict())
    db.add(new_instructor)
    db.commit()
    db.refresh(new_instructor)
    return new_instructor

# Update an existing instructor
@app.put("/instructors/{instructor_id}")
def update_instructor(instructor_id: int, instructor: UpdateInstructorSchema, db: Session = Depends(get_db)):
    existing_instructor = db.query(Instructors).filter(Instructors.id == instructor_id).first()
    if not existing_instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    for key, value in instructor.dict(exclude_unset=True).items():
        setattr(existing_instructor, key, value)
    db.commit()
    db.refresh(existing_instructor)
    return existing_instructor

# Delete an instructor
@app.delete("/instructors/{instructor_id}")
def delete_instructor(instructor_id: int, db: Session = Depends(get_db)):
    instructor = db.query(Instructors).filter(Instructors.id == instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    db.delete(instructor)
    db.commit()
    return {"message": f"Instructor {instructor_id} deleted successfully"}

# ---------- Course Routes ----------

# Get all courses
@app.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(Courses).all()
    return courses

# Get a single course by ID
@app.get("/courses/{course_id}")
def get_single_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Courses).filter(Courses.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

# Create a new course
@app.post("/courses")
def create_course(course: CreateCourseSchema, db: Session = Depends(get_db)):
    new_course = Courses(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

# Update an existing course
@app.put("/courses/{course_id}")
def update_course(course_id: int, course: UpdateCourseSchema, db: Session = Depends(get_db)):
    existing_course = db.query(Courses).filter(Courses.id == course_id).first()
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in course.dict(exclude_unset=True).items():
        setattr(existing_course, key, value)
    db.commit()
    db.refresh(existing_course)
    return existing_course

# Delete a course
@app.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Courses).filter(Courses.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return {"message": f"Course {course_id} deleted successfully"}
