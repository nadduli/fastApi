from typing import Optional
from fastapi import FastAPI, Response,status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()


class Post(BaseModel):
    title: str
    content:str
    published: bool = True
    rating: Optional[int] = None

try:
    conn = psycopg2.connect(host='localhost', database='fastApi', user='postgres', password='danny', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Successfully connected to the database")

except Exception as error:
    print("Database connection failed !")


my_posts = [{"title": "Title for post 1", "content": "content for post 1", "id": 1},
            {"title": "pirates", "content": "pirates of the caribbean", "id": 2},
            {"title": "favorite foods", "content": "rice, matooke and meat", "id": 3 }]

def find_post(id: int):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/")
async def root():
    return {"message": "welcome to my fast api service"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"message": posts}

@app.post("/posts", status_code= status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"post": post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id {id} was not found")
    return {"data": post}


@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail= f"post with id {id} doesnot exists")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail= f"post with id {id} doesnot exists")

    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"data": post_dict}


    return {"message": "updated post"}
    
    