from Compare import *
import json
from pymongo import MongoClient

MONGO_DB_HOST = "localhost"
MONGO_DB_PORT = "27017"
DB_NAME = "dbsdatabase"

UPLOAD_DOCUMENT_TABLE_NAME='dbsdatabase'

client = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(db=DB_NAME):
    db = client[db]
    return db


def get_relatedDocument(DocumentName):
    print("start")
    db=get_db()
    dbsdatabase=db['dbsdatabase']
    print(dbsdatabase)

    # if dbsdatabase.count()<3:
    #     print("Dbs database has less than 3 documents")



    OneDocument=dbsdatabase.find({'DocumentName':DocumentName})
    # documents = list(db[UPLOAD_DOCUMENT_TABLE_NAME].find({'KeyWords':"KeyWords"}))
    #
    print(OneDocument[0]['KeyWords'])
    print("after")
    AllDocument=dbsdatabase.find()
    # print(list(AllDocument))
    # fruits = ["apple", "banana", "cherry"]

    arrayforResult=[]
    arrayforDict=[]
    d={}

    print("before for loop")
    for x in AllDocument:
        # print (x['KeyWords'])
        if 'KeyWords' in x.keys():

          x1=x['KeyWords']
          str1 = ''.join(x1)

          print("str1=",str1)

        x2=OneDocument[0]['KeyWords']
        str2 = ''.join(x2)

        print("str2=",str2)

        vector1 = text_to_vector(str1)
        vector2 = text_to_vector(str2)

        result=get_cosine(vector1,vector2)

        print("result", result)

        arrayforResult.append(result)
        print("arrayforResult= ",arrayforResult)
        # d[x['SN']]=result
        d[x['DocumentName']]=result
        print("dicitongary= " ,d)



    max0=max(arrayforResult)
    arrayforResult.remove(max0)
    print("max0 ",max0)

    max1=max(arrayforResult)
    arrayforResult.remove(max1)
    print("max1 ",max1)
    #
    max2=max(arrayforResult)
    arrayforResult.remove(max2)
    print("max2 ",max2)


    print("before show keys")
    keys = []
    for key, value in d.items():
        if value == max0:
            print (key)
            SN=key

    for key, value in d.items():
        if value == max1:
            print (key)
            SN1=key

    for key, value in d.items():
        if value == max2:
            print (key)
            SN2=key

    resultarray=[]

    resultarray.append(SN)
    resultarray.append(SN1)
    resultarray.append(SN2)

    print("resultarray= ",resultarray)
    d={}
    d["1"]=resultarray[1]
    d["2"]=resultarray[2]

    return d
