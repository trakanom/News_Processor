import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("NEWS_API_KEY")
    SESSION_TYPE = "filesystem"
