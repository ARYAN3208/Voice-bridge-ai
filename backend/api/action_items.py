from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.ai_service import ai_service

router = APIRouter(
    prefix="/action-items",
    tags=["Action Items"],
)


class ActionItemsRequest(BaseModel):
    text: str


@router.post("/")
async def extract_action_items(
    request: ActionItemsRequest,
):
    try:

        action_items = await ai_service.extract_action_items(
            text=request.text,
        )

        return {
            "success": True,
            "message": "Action items extracted successfully.",
            "data": action_items,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )