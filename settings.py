import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    DATABASE = os.getenv('DATABASE', '')
    DATABASE_USER = os.getenv('DATABASE_USER', '')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '')
    DATABASE_HOST = os.getenv('DATABASE_HOST', '')
    DATABASE_PORT = os.getenv('DATABASE_PORT', '')
