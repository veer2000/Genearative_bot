from dotenv import load_dotenv
from fastapi import FastAPI
import requests

from src.chatbot import  chat_bot

load_dotenv()
app = FastAPI(
    title='ChatBot API',
)
print('at main')
app.include_router(chat_bot.app)

@app.get('/')
def home():
    return {'message': ' to ChatBot API!'}