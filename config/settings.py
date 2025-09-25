from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
API_BASE_URL = os.getenv("API_BASE_URL")

if not all([API_KEY, API_SECRET, API_BASE_URL]):
    raise ValueError("API_KEY, API_SECRET, and API_BASE_URL must be set in .env")
