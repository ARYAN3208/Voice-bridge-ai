from fastapi import APIRouter

router = APIRouter(
    prefix="/voice",
    tags=["Voice"]
)


@router.post("/record")
async def record_voice():
    return {
        "message": "Voice recording endpoint"
    }


@router.post("/upload")
async def upload_voice():
    return {
        "message": "Voice upload endpoint"
    }


@router.post("/transcribe")
async def transcribe_voice():
    return {
        "message": "Speech to text endpoint"
    }


@router.post("/translate")
async def translate_voice():
    return {
        "message": "Voice translation endpoint"
    }


@router.post("/synthesize")
async def synthesize_voice():
    return {
        "message": "Text to speech endpoint"
    }


@router.post("/conversation")
async def conversation_mode():
    return {
        "message": "Conversation mode endpoint"
    }


@router.get("/{voice_id}")
async def get_voice(voice_id: int):
    return {
        "message": f"Voice note {voice_id}"
    }


@router.get("/{voice_id}/transcript")
async def get_transcript(voice_id: int):
    return {
        "message": f"Transcript for voice note {voice_id}"
    }


@router.get("/{voice_id}/translation")
async def get_translation(voice_id: int):
    return {
        "message": f"Translation for voice note {voice_id}"
    }


@router.get("/{voice_id}/audio")
async def get_translated_audio(voice_id: int):
    return {
        "message": f"Translated audio for voice note {voice_id}"
    }


@router.delete("/{voice_id}")
async def delete_voice(voice_id: int):
    return {
        "message": f"Voice note {voice_id} deleted"
    }