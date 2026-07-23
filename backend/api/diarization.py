from pathlib import Path
import shutil
import uuid

from fastapi import APIRouter, File, HTTPException, UploadFile

from services.ai_service import ai_service

router = APIRouter(
    prefix="/diarization",
    tags=["Speaker Diarization"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/")
async def diarize_audio(
    file: UploadFile = File(...),
    language: str | None = None,
):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file uploaded.",
        )

    extension = Path(file.filename).suffix
    filename = f"{uuid.uuid4()}{extension}"
    file_path = UPLOAD_DIR / filename

    try:

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = await ai_service.diarize_audio(
            audio_path=str(file_path),
            language=language,
        )

        return {
            "success": True,
            "message": "Speaker diarization completed successfully.",
            "data": result,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:
        file.file.close()