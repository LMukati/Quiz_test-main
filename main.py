from fastapi import FastAPI
import uvicorn
from Routers import test,question,user

app = FastAPI()


app.include_router(test.router)
app.include_router(question.router)
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)