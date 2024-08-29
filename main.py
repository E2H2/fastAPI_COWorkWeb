from fastapi import FastAPI

from domain.detail import detail_router
from domain.comment import comment_router

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "이건 Moon의 repo야"}

app.include_router(detail_router.router)
app.include_router(comment_router.router)