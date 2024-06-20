import uvicorn
from fastapi import FastAPI

from routes.Routes import *

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", reload=True)
    except Exception as e:
        print("Not able to run the server. Error: ", e)