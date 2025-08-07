from fastapi import APIRouter

import os
import sys

from src.services.llm_service import geminillm
from src.services.memory_manager import memeorymanager

app = APIRouter()


print('Entered chat_bot file')
@app.post('/chat')
def chat_process(user_input: str):
    try:
        print('inside function chat_process')
        history = memeorymanager.get_history()
        response = geminillm.generate_response(user_input,history)

        memeorymanager.add_message("user",user_input)
        memeorymanager.add_message("ai",response)
        print(response)
        return {'result': response}
    except  Exception as e:
        print(e)