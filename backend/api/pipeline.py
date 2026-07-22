from pathlib import Path
import shutil
import uuid

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from services.ai_service import ai_service

router = APIRouter(
    prefix="/pipeline",
    tags=["AI Pipeline"],
)

UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/")
async def process_pipeline(
    file: UploadFile = File(...),
    source_language: str = Form("en"),
    target_language: str = Form("hi"),
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file uploaded.",
        )

    extension = Path(file.filename).suffix

    input_filename = f"{uuid.uuid4()}{extension}"
    input_path = UPLOAD_DIR / input_filename

    output_filename = f"{uuid.uuid4()}.mp3"
    output_path = OUTPUT_DIR / output_filename

    with input_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:

        result = await ai_service.process_pipeline(
            audio_path=str(input_path),
            source_language=source_language,
            target_language=target_language,
            output_audio_path=str(output_path),
        )

        result["audio_file"] = str(output_path)

        return {
            "success": True,
            "message": "Pipeline completed successfully.",
            "data": result,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:

        file.file.close()