from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "THEMIS"
    API_V1_STR: str = "/api"
    # Postgres
    POSTGRES_URL: str = "postgresql://postgres:postgres@localhost:5432/themis"

    # LLM
    GEMINI_API_KEY: str | None = None
    GROQ_API_KEY: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
