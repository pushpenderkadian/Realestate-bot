import datetime
import requests
from settings import WABAURL, WABAHEADER
import database 

def send_text_message(msgdata, message):
    data={
      "messaging_product": "whatsapp",
      "recipient_type": "individual",
      "to": msgdata,
      "type": "text",
      "text": { 
        "preview_url": False,
        "body": message
        }
    }
    response = requests.post(WABAURL, headers=WABAHEADER, json=data)
    
    print(response.status_code)
    print(response.json())

def send_payload_message(payload):
    response = requests.post(WABAURL, headers=WABAHEADER, json=payload)
    
    if response.status_code ==200:
        print("Message sent successfully")
        database.users.update_one({"contact":payload["to"]},{"$set":{"last_msg_payload":payload}})
    else:
        print(response.status_code)
        print(response.text)

def extract_contact(msgdata):
    try:
        return msgdata["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
    except:
        return None

def extract_text_message(msgdata):
    try:
        if msgdata["entry"][0]["changes"][0]["value"]["messages"][0]["type"]=="text":
            return msgdata["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        else:
            return None
    except:
        return None

def extract_button_message(msgdata):
    try:
        if msgdata["entry"][0]["changes"][0]["value"]["messages"][0]["type"]=="interactive":
            if msgdata["entry"][0]["changes"][0]["value"]["messages"][0]["interactive"]["type"]=="button_reply":
                return msgdata["entry"][0]["changes"][0]["value"]["messages"][0]["interactive"]["button_reply"]
            else:
                return None
        else:
            return None
    except:
        return None    
def extract_list_reply(msgdata):
    try:
        if msgdata["entry"][0]["changes"][0]["value"]["messages"][0]["type"]=="interactive":
            if msgdata["entry"][0]["changes"][0]["value"]["messages"][0]["interactive"]["type"]=="list_reply":
                return msgdata["entry"][0]["changes"][0]["value"]["messages"][0]["interactive"]["list_reply"]
            else:
                return None
        else:
            return None
    except:
        return None
def create_new_user(contact):
    data={
        "contact": contact,
        "language": "english",
        "current_step": 0,
        "last_msg_payload": None,
        "created_at": datetime.datetime.utcnow(),
        "name":None
    }
    database.users.insert_one(data)

def check_user(contact):
    userdetials=database.users.find_one({"contact":contact})
    if userdetials:
        return True
    else:
        create_new_user(contact)
        return False

def get_user_current_step(contact):
    userdetials=database.users.find_one({"contact":contact})
    if userdetials:
        return userdetials["current_step"]
    else:
        return 0
def set_user_current_step(contact,step):
    database.users.update_one({"contact":contact},{"$set":{"current_step":step}})

def set_user_language(contact,language):
    database.users.update_one({"contact":contact},{"$set":{"language":language}})

def add_user_requirements(contact,type):
    if database.requirements.find_one({"contact":contact,"flow_completed":False}):
        database.requirements.update_one({"contact":contact,"flow_completed":False},{"$set":{"type":type,type:{}}})
    else:
        database.requirements.insert_one({"contact":contact,"type":type,type:{},"flow_completed":False,"created_at":datetime.datetime.utcnow(),"updated_at":datetime.datetime.utcnow()})

def add_user_requirements_pg(contact,pgfield,pgvalue):
    database.requirements.update_one({"contact":contact,"flow_completed":False},{"$set":{f"pg.{pgfield}":pgvalue}})

def get_user_requirements_pg(contact,pgfield):
    return database.requirements.find_one({"contact":contact,"flow_completed":False}).get("pg").get(pgfield)

def add_user_requirements_flat(contact,flatfield,flatvalue):
    database.requirements.update_one({"contact":contact,"flow_completed":False},{"$set":{f"flat.{flatfield}":flatvalue}})

def get_user_requirements_flat(contact,flatfield):
    return database.requirements.find_one({"contact":contact,"flow_completed":False}).get("flat").get(flatfield)

def get_user_requirements(contact):
    return database.requirements.find_one({"contact":contact,"flow_completed":False})["type"]
def complete_flow(contact):
    database.requirements.update_one({"contact":contact,"flow_completed":False},{"$set":{"flow_completed":True,"updated_at":datetime.datetime.utcnow()}})
    database.users.update_one({"contact":contact},{"$set":{"current_step":[1,False]}})