from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from aksharamukha import transliterate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

class TextRequest(BaseModel):
    text: str

def transliterate_text(text : str) -> str:
    return transliterate.process("autodetect", "ISO", text)

@app.post("/transliterate")
async def transiterated_text(input_text: TextRequest):
    text = input_text.text
    result = transliterate_text(text)
    return {'transiterated_text':result}



