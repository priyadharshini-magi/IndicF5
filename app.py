from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import edge_tts
import uuid
import os
import asyncio

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


OUTPUT_DIR = "generated_audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)


class TTSRequest(BaseModel):
    text: str
    language: str


# Language -> Voice mapping
VOICE_MAP = {
    "tamil": ["ta-IN-PallaviNeural", "ta-IN-PrabhaNeural", "ta-IN-ValluvarNeural",
 "ta-IN-TamilVoice1", "ta-IN-TamilVoice2", "ta-IN-TamilVoice3",
 "ta-IN-TamilVoice4", "ta-IN-TamilVoice5", "ta-IN-TamilVoice6", "ta-IN-TamilVoice7"]
,
    "english": ["en-IN-NeerjaNeural","en-IN-AashiNeural","en-IN-AaravNeural",
 "en-IN-AnanyaNeural","en-IN-KavyaNeural","en-IN-KunalNeural",
 "en-IN-RehaanNeural","en-IN-PrabhatNeural","en-IN-EnglishVoice9",
 "en-IN-EnglishVoice10"]
,
    "hindi": ["hi-IN-SwaraNeural","hi-IN-AaravNeural","hi-IN-AnanyaNeural",
 "hi-IN-KavyaNeural","hi-IN-KunalNeural","hi-IN-RehaanNeural",
 "hi-IN-HindiVoice7","hi-IN-HindiVoice8","hi-IN-HindiVoice9",
 "hi-IN-HindiVoice10"]
,
    "telugu": ["te-IN-ShrutiNeural","te-IN-MohanNeural",
 "te-IN-TeluguVoice3","te-IN-TeluguVoice4","te-IN-TeluguVoice5",
 "te-IN-TeluguVoice6","te-IN-TeluguVoice7","te-IN-TeluguVoice8",
 "te-IN-TeluguVoice9","te-IN-TeluguVoice10"]
,
    "kannada": ["kn-IN-SapnaNeural","kn-IN-VishnuNeural","kn-IN-GowriNeural",
 "kn-IN-KannadaVoice4","kn-IN-KannadaVoice5","kn-IN-KannadaVoice6",
 "kn-IN-KannadaVoice7","kn-IN-KannadaVoice8","kn-IN-KannadaVoice9",
 "kn-IN-KannadaVoice10"]
,
    "malayalam": ["ml-IN-SobhanaNeural","ml-IN-MidhunNeural","ml-IN-AnilaNeural",
 "ml-IN-MalayalamVoice4","ml-IN-MalayalamVoice5","ml-IN-MalayalamVoice6",
 "ml-IN-MalayalamVoice7","ml-IN-MalayalamVoice8","ml-IN-MalayalamVoice9",
 "ml-IN-MalayalamVoice10"]

}


@app.post("/generate")
async def generate_audio(data: TTSRequest):
    
    voice = VOICE_MAP.get(data.language)

    filename = f"{uuid.uuid4()}.wav"
    filepath = os.path.join(OUTPUT_DIR, filename)

    communicate = edge_tts.Communicate(data.text, voice)
    await communicate.save(filepath)

    return {"file": filename}


@app.get("/audio/{filename}")
def get_audio(filename: str):
    path = os.path.join(OUTPUT_DIR, filename)
    return FileResponse(path, media_type="audio/wav")
