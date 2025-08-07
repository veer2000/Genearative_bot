from fastapi import FastAPI
import requests

from src.chatbot import  chat_bot


app = FastAPI(
    title='ChatBot API',
)

app.include_router(chat_bot.app)


@app.get('/')
def home():
    return {'message': 'Welcome to ChatBot API!'}