import os


def get_env() -> str:
    app_env = os.getenv("APP_ENV", None)

    match app_env:
        case "local":
            return "./.env.local"
        case "dev":
            return "./.env.dev"
        case _:
            return "./.env.local"
