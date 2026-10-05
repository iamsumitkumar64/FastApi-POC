from pydantic_settings import BaseSettings,SettingsConfigDict

class EnvConfig(BaseSettings):
    PORT: int = 8000
    HOSTNAME: str = '0.0.0.0'

model_config = SettingsConfigDict(
    env_file = ".env",
    env_file_encoding = "utf-8",
    case_sensitive = True,
)

envConfig = EnvConfig()