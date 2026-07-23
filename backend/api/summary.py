from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.ai_service import ai_service

router = APIRouter(
    prefix="/summary",
    tags=["Summary"],
)


class SummaryRequest(BaseModel):
    text: str


@router.post("/")
async def generate_summary(
    request: SummaryRequest,
):
    try:

        summary = await ai_service.summarize_text(
            text=request.text,
        )

        return {
            "success": True,
            "message": "Summary generated successfully.",
            "data": summary,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )