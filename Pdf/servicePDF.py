from flask import Flask,jsonify,request
# from flask import request
from flask_restful import Resource, Api
from json import dumps
from bson import json_util

# import mongodb_client
from datetime import datetime

import operations as op
import Get_keyword_sentiment_entity as keyword_sentiment_entity
import CopyPaste as cp
import GetRelatedDoc as Gr
import CopyPaste as cp
import GetRelatedDoc as getrelated
#add for test
import PPTtoPDF as Topdf


CLICK_LOGS_TABLE_NAME = 'dbsdatabase'
UPLOAD_DOCUMENT_TABLE_NAME='dbsdatabase'



app = Flask(__name__)
api = Api(app)

# '''test method'''
# @app.route("/json_example", methods=['POST'])
# def json_example():
#     req_data = request.get_json()
#
#     language = req_data.get("language")
#
#     return language

#Keyword Confirmation Page
@app.route("/keywordsConfirmation", methods=['POST'])
def keywordsConfirmation():
    req_data = request.get_json()

    Entities=req_data.get("Entity")
    DocumentName=req_data.get("FileName")
    KeyWords=req_data.get("Keyword")
    Location=req_data.get("Location")
    MeetingType=req_data.get("Type")
    Month=req_data.get("Month")
    Sensitive=req_data.get("Sensitive")
    Year=req_data.get("Year")

    # SN=req_data.get("SN")
    # DocumentName=req_data.get("FileName")
    #
    # ImportantLevel=req_data.get("ImportantLevel")
    # Author=req_data.get("Author")
    op.UploadDocument(DocumentName,Location,MeetingType,Year,Month,"Employee_Name",KeyWords,Entities,Sensitive)
    # UploadDocument(DocumentName,Location,MeetingType,Year,Month,Employee_Name,KeyWords,Entities,sensitive):

    # op.UploadDocument(SN,DocumentName,Location,MeetingType,Year,Month,ImportantLevel,Author,KeyWords,Entities)
    dict={"key":"Success"}
    result=dumps(dict,default=json_util.default)
    return result


@app.route('/getDocumentByKeywords', methods=['GET'])
def getDocumentByKeywords():
    keyword = request.args.get('keyword')

    temp=op.GetDocumentByKeywords(keyword)

    result=dumps(temp[0],default=json_util.default)

    return result

@app.route('/test', methods=['GET'])
def test():
    Topdf.PPTtoPDF("abcd.pptx","topdf.pdf")

    # print ('test_basic passed!')
    # Dict=keyword_sentiment_entity.Get_keyword_sentiment_entity_dictionary("abcd.pptx")

#Upload Page
@app.route('/uploadPageSubmit', methods=['POST'])
def uploadPageSubmit():
    req_data = request.get_json()

    filepath = req_data.get('fileInput')
    DocumentName=filepath


    Dict=keyword_sentiment_entity.Get_keyword_sentiment_entity_dictionary(filepath)

    KeyWords=Dict["keyword"]
    Sentiments=Dict["sentiment"]
    Entities=Dict["entity"]

    Employee_Name= req_data.get('Employee_Name')
    Location= req_data.get('location')
    Month= req_data.get('month')
    Year= req_data.get('year')
    MeetingType= req_data.get('type')
    sensitive= req_data.get('sensitive')

    to_path ="C:\Findingaudit\Rawdata\\"
    # to_path= to_path+Location+"\\"
    from_path="C:\Findingaudit\\"
    cp.copypaste(from_path,to_path,DocumentName)

    # op.UploadDocument(DocumentName,Location,MeetingType,Year,Month,Employee_Name,KeyWords,Entities,sensitive)

    # a={"abd":"dd"}
    app.logger.info('%s filepath', filepath)

    z = {**Dict, **req_data}
    result=dumps(z,default=json_util.default)

    return result

@app.route('/searchPage', methods=['POST'])
def searchPage():
    req_data = request.get_json()

    Employee_Name=req_data.get('Employee_Name')
    location=req_data.get('location')
    sensitive=req_data.get('sensitive')
    type=req_data.get('type')
    # keyword=req_data.get('keyword')
    keyword=req_data.get('undefined')
    # year=req_data.get('year')
    # month=req_data.get('month')
    # keyword=req_data.get('keyword')

    # author=req_data.get('importantlevel')

    # importantlevel=req_data.get('importantlevel')
    # meetingType=req_data.get('meetingType')

    temp=op.GetDocumentBySearch(Employee_Name,location,sensitive,type,keyword)

    arrayResult=[]

    if len(temp)==0:
        result="fail"
    else:
        # dict={}

        for x in temp:
            dict={}

            dict["SN"]=x["SN"]
            dict["DocumentName"]=x["DocumentName"]
            dict["Year"]=x["Year"]
            dict["Month"]=x["Month"]
            dict["KeyWords"]=x["KeyWords"][:5]
            dict["Entities"]=x["Entities"]
            # dict["Entities"]="hardcode in api"
            arrayResult.append(dict)


        # result=dumps(temp,default=json_util.default)
        result=dumps(arrayResult,default=json_util.default)
        ### after testing must be deleted
        # testResult=dumps(testdict,default=json_util.default)

    return result

@app.route('/Review', methods=['POST'])
def Review():
    req_data = request.get_json()

    DocumentName=req_data.get("DocumentName")


    temp=getrelated.get_relatedDocument(DocumentName)
    result=dumps(temp,default=json_util.default)
    return result



class Employees(Resource):
    def get(self):
        # conn = db_connect.connect() # connect to database
        # query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': ["test employees"]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        # conn = db_connect.connect()
        # query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': ["also a test"]}
        return jsonify(result)

# class Employees_Name(Resource):
#     def get(self, employee_id):
#         conn = db_connect.connect()
#         query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')
