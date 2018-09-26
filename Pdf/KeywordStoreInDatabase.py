from pymongo import MongoClient
from Get_keyword_sentiment_entity import *
from datetime import datetime

MONGO_DB_HOST = "localhost"
MONGO_DB_PORT = "27017"
DB_NAME = "dbsdatabase"

CLICK_LOGS_TABLE_NAME = 'dbsdatabase'
UPLOAD_DOCUMENT_TABLE_NAME='dbsdatabase'

client = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(db=DB_NAME):
    db = client[db]
    return db



def UploadDocument(DocumentName,Location,type,Year,Month,ImportantLevel,Employee_Name,Filepath,sensitive):
    db = get_db()
    count=db[UPLOAD_DOCUMENT_TABLE_NAME].count()
    SN="sn"+str(count)

    dict=Get_keyword_sentiment_entity_dictionary(Filepath)
    KeyWords=dict["keyword"]
    Entities=dict["entity"]
    Sentiments=dict["sentiment"]

    message = {'SN': SN, 'DocumentName': DocumentName,'Location':Location, 'type':type,
    'Year':Year,'Month':Month,'ImportantLevel':ImportantLevel,'Employee_Name':Employee_Name,'KeyWords':KeyWords,
    'Entities':Entities,'Sentiments':Sentiments,'timestamp': datetime.utcnow(),'Filepath':Filepath,'sensitive':sensitive}


    db[UPLOAD_DOCUMENT_TABLE_NAME].insert(message)
