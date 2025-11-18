import asyncio
import base64
import io

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from googletrans import Translator
from gtts import gTTS
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TranslateRequest(BaseModel):
    source: str
    target: str
    text: str


class TTSRequest(BaseModel):
    text: str
    lang: str


@app.post("/translate")
async def translate_text(req: TranslateRequest):
    async with Translator() as translator:
        result = await translator.translate(req.text, src=req.source, dest=req.target)
        return PlainTextResponse(result.text)


@app.post("/tts")
async def text_to_speech(req: TTSRequest):
    def generate_audio():
        tts = gTTS(text=req.text, lang=req.lang)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        return base64.b64encode(buf.read()).decode("utf-8")

    audio_base64 = await asyncio.to_thread(generate_audio)
    return PlainTextResponse(audio_base64)
