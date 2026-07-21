from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
async def register():
    return {
        "message": "Register endpoint"
    }


@router.post("/login")
async def login():
    return {
        "message": "Login endpoint"
    }


@router.post("/forgot-password")
async def forgot_password():
    return {
        "message": "Forgot Password endpoint"
    }


@router.post("/reset-password")
async def reset_password():
    return {
        "message": "Reset Password endpoint"
    }


@router.get("/me")
async def get_current_user():
    return {
        "message": "Current User endpoint"
    }