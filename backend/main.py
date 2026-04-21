from fastapi import FastAPI
from pydantic import BaseModel
from hashtag_engine import generate_hashtags

app = FastAPI()

class Request(BaseModel):
    text: str

@app.post("/generate")
def generate(req: Request):
    return {
        "input": req.text,
        "hashtags": generate_hashtags(req.text)
    }
