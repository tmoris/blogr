import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Basic configurations
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Secret_key configurations
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = os.environ.get("DEBUG") or True

    # Database configurations
    DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATION = False
