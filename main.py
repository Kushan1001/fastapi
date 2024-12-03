from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from deep_translator import GoogleTranslator

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

@app.get('/')
def homepage():
    return {"message": "success"}

@app.post("/transliterate")
async def transiterated_text(input_text: TextRequest):
    text = input_text.text
    result = GoogleTranslator(source='auto', target='en').translate(text)
    return {'transiterated_text':result}



