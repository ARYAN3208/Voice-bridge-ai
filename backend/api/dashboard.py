from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
async def get_dashboard():
    return {
        "message": "Dashboard endpoint"
    }


@router.get("/stats")
async def get_dashboard_stats():
    return {
        "message": "Dashboard statistics endpoint"
    }


@router.get("/recent")
async def get_recent_activity():
    return {
        "message": "Recent activity endpoint"
    }


@router.get("/overview")
async def get_overview():
    return {
        "message": "Overview endpoint"
    }


@router.get("/ai-status")
async def get_ai_status():
    return {
        "message": "AI status endpoint"
    }


@router.get("/quick-actions")
async def get_quick_actions():
    return {
        "message": "Quick actions endpoint"
    }


@router.get("/notifications")
async def get_notifications():
    return {
        "message": "Notifications endpoint"
    }


@router.get("/system-health")
async def get_system_health():
    return {
        "message": "System health endpoint"
    }