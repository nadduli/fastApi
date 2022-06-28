from fastapi import FastAPI
#from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content:str 

@app.get("/")
async def root():
    return {"message": "welcome to my fast api service"}


@app.get("/posts")
def get_posts():
    return {"message": "retrieve my posts"}

@app.post("/create_posts")
def create_posts(new_post : Post):
    print(new_post)
    return {"data": "new posts"}