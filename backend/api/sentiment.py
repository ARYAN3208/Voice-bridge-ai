from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.ai_service import ai_service

router = APIRouter(
    prefix="/sentiment",
    tags=["Sentiment"],
)


class SentimentRequest(BaseModel):
    text: str


@router.post("/")
async def analyze_sentiment(
    request: SentimentRequest,
):
    try:

        sentiment = await ai_service.analyze_sentiment(
            text=request.text,
        )

        return {
            "success": True,
            "message": "Sentiment analysis completed successfully.",
            "data": sentiment,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )