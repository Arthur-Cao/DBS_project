
import mongodb_client
from datetime import datetime

CLICK_LOGS_TABLE_NAME = 'dbsdatabase'
UPLOAD_DOCUMENT_TABLE_NAME='dbsdatabase'


def UploadDocument(DocumentName,Location,MeetingType,Year,Month,Employee_Name,KeyWords,Entities,sensitive):
    db = mongodb_client.get_db()
    count=db[UPLOAD_DOCUMENT_TABLE_NAME].count()
    SN="sn"+str(count)

    message = {'SN': SN, 'DocumentName': DocumentName,'Location':Location, 'MeetingType':MeetingType,
    'Year':Year,'Month':Month,'Employee_Name':Employee_Name,'KeyWords':KeyWords,
    'Entities':Entities,'timestamp': datetime.utcnow(),"sensitive":sensitive}


    db[UPLOAD_DOCUMENT_TABLE_NAME].insert(message)
# Employee_Name,location,sensitive,type
def GetDocumentBySearch(Employee_Name,location,sensitive,type,keyword):
     db = mongodb_client.get_db()

     d={}
     if  Employee_Name!=None:
        d["Employee_Name"]=Employee_Name

     if  location!=None:
        d["Location"]=location

     if  sensitive!=None:
        d["sensitive"]=sensitive

     if  type!=None:
        d["MeetingType"]=type

     if keyword!="":
        d["KeyWords"]=keyword



     documents = list(db[UPLOAD_DOCUMENT_TABLE_NAME].find(d))
     # documents = list(db[UPLOAD_DOCUMENT_TABLE_NAME].find({'Employee_Name':"danial"}))
     print (documents)
     return documents



def GetDocumentByKeywords(keywords):
     db = mongodb_client.get_db()
     documents = list(db[UPLOAD_DOCUMENT_TABLE_NAME].find({'KeyWords':keywords}))
     print (documents)
     return documents
