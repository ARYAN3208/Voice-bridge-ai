from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.ai_service import ai_service

router = APIRouter(
    prefix="/translation",
    tags=["Translation"],
)


class TranslationRequest(BaseModel):
    text: str
    source_language: str
    target_language: str


@router.post("/")
async def translate_text(
    request: TranslationRequest,
):
    try:

        translation = await ai_service.translate_text(
            text=request.text,
            source_language=request.source_language,
            target_language=request.target_language,
        )

        return {
            "success": True,
            "message": "Translation completed successfully.",
            "data": {
                "original_text": request.text,
                "translated_text": translation,
                "source_language": request.source_language,
                "target_language": request.target_language,
            },
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )