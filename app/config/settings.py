from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Aplication
    app_name: str
    app_version: str
    app_description: str

    # Database
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @property
    def database_url(self) -> str:
        return (f"postgresql+psycopg://{self.db_user}:{self.db_password}"
                f"@{self.db_host}:{self.db_port}/{self.db_name}")
    # La string que construye la función
    # "postgresql://:postgres:qwerty@localhost:5432/ecommerce_fem"



settings = Settings()

