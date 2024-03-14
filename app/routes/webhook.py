from fastapi import APIRouter,Request
import app.bot as bot
import json
import app.utils as utils


router = APIRouter()

@router.get("/webhook")
async def setwebhook(request: Request):
    return int(request.query_params.get("hub.challenge"))

@router.post("/webhook")
async def webhook(request: Request):
    msgdata = await request.json()
    
    if utils.extract_text_message(msgdata) or utils.extract_button_message(msgdata) or utils.extract_list_reply(msgdata):
        print(msgdata)
        bot.startflow(msgdata)
    return {"message": "Hello World"}
