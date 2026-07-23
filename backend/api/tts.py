from pathlib import Path
import uuid

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.ai_service import ai_service

router = APIRouter(
    prefix="/tts",
    tags=["Text To Speech"],
)

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class TTSRequest(BaseModel):
    text: str
    voice: str = "aura-2-thalia-en"


@router.post("/")
async def generate_speech(
    request: TTSRequest,
):
    try:

        output_filename = f"{uuid.uuid4()}.mp3"
        output_path = OUTPUT_DIR / output_filename

        result = await ai_service.generate_speech(
            text=request.text,
            output_path=str(output_path),
            voice=request.voice,
        )

        return {
            "success": True,
            "message": "Speech generated successfully.",
            "data": {
                "audio_file": str(output_path),
                "tts_result": result,
            },
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )