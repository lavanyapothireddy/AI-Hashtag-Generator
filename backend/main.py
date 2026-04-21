from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from hashtag_engine import generate_hashtags

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Request(BaseModel):
    text: str

@app.post("/generate")
def generate(req: Request):
    tags = generate_hashtags(req.text)
    return {"hashtags": tags}
