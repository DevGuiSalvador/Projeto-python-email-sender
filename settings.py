import os
from dotenv import load_dotenv

load_dotenv()

APP_EMAIL_SECRET = os.getenv("APP_EMAIL")
APP_PASSWORD_SECRET = os.getenv("APP_PASSWORD")
