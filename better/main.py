import uvicorn
from fastapi import FastAPI
from better.app.controller.user_controller import UserService

app = FastAPI()

app.include_router(UserService.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)