from typing import Optional
from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content:str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "Title for post 1", "content": "content for post 1", "id": 1},
            {"title": "pirates", "content": "pirates of the caribbean", "id": 2},
            {"title": "favorite foods", "content": "rice, matooke and meat", "id": 3 }]

def find_post(id: int):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
async def root():
    return {"message": "welcome to my fast api service"}


@app.get("/posts")
def get_posts():
    return {"message": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"post": post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(int(id))
    if not post:
        response.status_code = 404
    return {"data": post}