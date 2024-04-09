from fastapi import FastAPI, Response, status
from routes.student import student
app = FastAPI()

app.include_router(student)
