from fastapi import APIRouter

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/")
async def get_analytics():
    return {
        "message": "Analytics endpoint"
    }


@router.get("/languages")
async def get_language_analytics():
    return {
        "message": "Language analytics endpoint"
    }


@router.get("/usage")
async def get_usage_analytics():
    return {
        "message": "Usage analytics endpoint"
    }


@router.get("/performance")
async def get_performance_analytics():
    return {
        "message": "Performance analytics endpoint"
    }


@router.get("/weekly")
async def get_weekly_analytics():
    return {
        "message": "Weekly analytics endpoint"
    }


@router.get("/monthly")
async def get_monthly_analytics():
    return {
        "message": "Monthly analytics endpoint"
    }


@router.get("/translation")
async def get_translation_analytics():
    return {
        "message": "Translation analytics endpoint"
    }


@router.get("/voice")
async def get_voice_analytics():
    return {
        "message": "Voice analytics endpoint"
    }