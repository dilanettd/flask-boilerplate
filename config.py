import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


def as_bool(value):
    if value:
        return value.lower() in ["true", "yes", "on", "1"]
    return False


class Config:
    # app  database options
    APIFAIRY_TITLE: str = os.getenv("BoilerPlate API")
    APIFAIRY_VERSION: str = os.getenv("1.0")
    APIFAIRY_UI: str = os.getenv("elements")
    USE_CORS = as_bool(os.getenv("USE_CORS") or "yes")
    CORS_SUPPORTS_CREDENTIALS = True
