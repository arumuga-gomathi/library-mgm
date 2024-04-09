from fastapi import APIRouter
from models.student import Student
from database import conn
from bson import ObjectId


student = APIRouter()

#creating routes

@student.post('/students',status_code=201)
def create_student(student:Student):
    print(student)
    dbres = conn.libmgmdb.students.insert_one(dict(student))
    print(dbres)
    return {"id": str(dbres.inserted_id)}

@student.get('/students')
def find_all_Students(country: str = None, age: int = None):
    students = conn.libmgmdb.students.find()
    if country:
        students = [student for student in students if student['address']['country'] == country]
    
    if age:
        students = [student for student in students if student.get('age') >= age]
    return [buildResponse(student) for student in students]

def buildResponse(student):
    return { "name": str(student['name']), "age": int(student['age'])}

@student.get('/students/{id}')
def find_all_Students(id: str):
    print(id)
    response = conn.libmgmdb.students.find_one({"_id": ObjectId(str(id))}, {'_id': 0})
    print(response)
    if response:
        return response

@student.patch('/students/{id}', status_code=204)
def find_all_Students(id: str, item: Student):
    print(id)
    conn.libmgmdb.students.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(item)})
    return {}

@student.delete('/students/{id}', status_code=200)
def find_all_Students(id: str):
    print(id)
    conn.libmgmdb.students.delete_one({"_id": ObjectId(id)})
    return {}