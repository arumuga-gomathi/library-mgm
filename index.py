from fastapi import FastAPI
from routes.student import student
from mangum import Mangum
import uvicorn
app = FastAPI()

app.include_router(student)

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)