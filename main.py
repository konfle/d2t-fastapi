from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/posts", status_code=201)
def create_post(payload: dict = Body(...)):
    return {
        "message": "successfully created a post",
        "post": {
            "title": payload['title'],
            "content": payload['content']
        }
    }
