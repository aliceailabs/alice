import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.ai import Gemini

'''
Routers within 'host/chat'
'''

router = APIRouter(
    prefix='/chat',
    tags=['chat'],
    responses={404: {'description': 'Not found'}},
)

api_key_gemini = os.getenv('API_KEY_GEMINI')
print(api_key_gemini)
provider = Gemini(api_key_gemini)


class ReqChat(BaseModel):
    text: str


def generate_text(text: str) -> str:
    try:
        reply = provider.send(req.text)
    except Exception as e:
        print('Exception:', e)
        reply = ''
    return reply


@router.post('/ask')
async def chat(req :ReqChat):
    if not req.text:
        return
    
    reply = generate_text(req.text)

    return {'reply': reply}
