# import fastapi
from fastapi import FastAPI

# initiate fastapi
app = FastAPI()

# define the routes now
@app.get('/')
def index():
    return {"message": "Welcome to MYO BIO MANAGEMENT SYSTEM"}


# GET -> retireve resourse
@app.get('/students') 
def students():
    return[]

# getting a single student
@app.get('/students/{student_id}')
def create_student( student_id: int):
    print(student_id)
    return {"message": f"student {student_id} fetched successfully"}

# POST -> create a resourse
@app.post('/students')
def create_student():
    return {"message": " student created successfully"}

# PUT/PATCH -> update a resourse
@app.patch('/students/{student_id}')
def update_student(student_id: int):
    print(student_id)
    return {"message": " student updated successfully"}

# DELETE -> deleting a resourse
@app.delete('/students/{student_id}')
def delete_student(student_id: int):
    print(student_id)
    return {"message": " student deleted successfully"}
