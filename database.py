from pymongo import MongoClient
from settings import settings

client=MongoClient(settings.MGDB)

db=client[settings.DBNAME]
users=db.users
requirements=db.requirements
temp_session=db.temp_session