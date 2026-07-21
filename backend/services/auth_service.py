from datetime import datetime


class AuthService:

    def register_user(self):
        return {
            "status": "success",
            "message": "User registered successfully",
            "timestamp": datetime.utcnow().isoformat()
        }

    def login_user(self):
        return {
            "status": "success",
            "message": "Login successful",
            "access_token": "",
            "refresh_token": ""
        }

    def forgot_password(self):
        return {
            "status": "success",
            "message": "Password reset link sent"
        }

    def reset_password(self):
        return {
            "status": "success",
            "message": "Password reset successful"
        }

    def get_current_user(self):
        return {
            "status": "success",
            "user": {}
        }


auth_service = AuthService()