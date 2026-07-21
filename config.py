from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    HOST: str
    PORT: int

    DATABASE_URL: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    DEEPGRAM_API_KEY: str = ""

    INDICTRANS_MODEL: str

    ELEVENLABS_API_KEY: str = ""

    SMALLEST_AI_API_KEY: str = ""

    OPENAI_API_KEY: str = ""

    GEMINI_API_KEY: str = ""

    CHROMA_DB_PATH: str

    UPLOAD_FOLDER: str
    MAX_UPLOAD_SIZE: int

    LOG_LEVEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()