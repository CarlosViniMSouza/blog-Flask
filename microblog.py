from dotenv import load_dotenv
from app import app
import os

load_dotenv()

name = os.getenv("FLASK_NAME")
env = os.getenv("FLASK_ENV")