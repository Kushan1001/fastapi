from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from aksharamukha import transliterate
from langdetect import detect
from ai4bharat.transliteration import XlitEngine


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

@app.get('/')
def homepage():
    return {'message': 'success'}

@app.post("/transliterate")
async def transiterated_text(input_text: TextRequest):
    text = input_text.text
    if detect(text) != 'fa' and detect(text) != 'ur':
        result = transliterate_text(text)
        return {'transiterated_text':result}
    else:
        e = XlitEngine(src_script_type="indic", beam_width=100, rescore=False)
        result = e.translit_word(text , lang_code="ur", topk=1)
        return {'transiterated_text': result}


