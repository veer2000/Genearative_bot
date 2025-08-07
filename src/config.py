import os
import sys

from dotenv import load_dotenv

load_dotenv()
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GemiApi:str = os.getenv('GEMKEY')
    ModelName:str = os.getenv('GEMMODEL')

settings = Settings()