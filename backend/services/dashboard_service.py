from datetime import datetime


class DashboardService:

    def get_dashboard(self):
        return {
            "status": "success",
            "timestamp": datetime.utcnow().isoformat()
        }

    def get_dashboard_stats(self):
        return {
            "status": "success",
            "total_translations": 0,
            "total_voice_notes": 0,
            "average_latency": 0,
            "supported_languages": 0
        }

    def get_recent_activity(self):
        return {
            "status": "success",
            "activities": []
        }

    def get_overview(self):
        return {
            "status": "success",
            "overview": {}
        }

    def get_ai_status(self):
        return {
            "status": "success",
            "speech_to_text": "offline",
            "translation": "offline",
            "text_to_speech": "offline",
            "llm": "offline"
        }

    def get_quick_actions(self):
        return {
            "status": "success",
            "actions": []
        }

    def get_notifications(self):
        return {
            "status": "success",
            "notifications": []
        }

    def get_system_health(self):
        return {
            "status": "success",
            "cpu_usage": 0,
            "memory_usage": 0,
            "disk_usage": 0
        }


dashboard_service = DashboardService()