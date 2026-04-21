from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from hashtag_engine import generate_hashtags

app = FastAPI()

# ✅ CORS FIX (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Request(BaseModel):
    text: str

@app.post("/generate")
def generate(req: Request):
    return {
        "input": req.text,
        "hashtags": generate_hashtags(req.text)
    }
