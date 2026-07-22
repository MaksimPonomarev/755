from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_URL: str
    login: str | None = None
    password: str | None = None
    headless: bool = True
    browser: str = "chromium"
    timeout: int
    slow_mo: int = 0

    # Новый формат конфигурации для Pydantic v2
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  
    )


settings = Settings()
