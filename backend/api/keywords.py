from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.ai_service import ai_service

router = APIRouter(
    prefix="/keywords",
    tags=["Keywords"],
)


class KeywordRequest(BaseModel):
    text: str


@router.post("/")
async def extract_keywords(
    request: KeywordRequest,
):
    try:

        keywords = await ai_service.extract_keywords(
            text=request.text,
        )

        return {
            "success": True,
            "message": "Keywords extracted successfully.",
            "data": keywords,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )