
from string_handle import *
import json
import os
import PPTtoPDF as converFormat

def Get_keyword_sentiment_entity_dictionary(OrignalFileName):

    pathstring=r"C:\Findingaudit\\"

    filename, file_extension = os.path.splitext(OrignalFileName)

    if file_extension==".pptx":
        input=pathstring+OrignalFileName

        suffix=".pdf"
        NewfileName=filename+suffix
        path=pathstring+NewfileName
        converFormat.PPTtoPDF(input,(pathstring+filename))
    else:
        suffix=".pdf"
        NewfileName=filename+suffix
        path=pathstring+NewfileName



    # keyword=generate_keyword(filename)
    #
    # sentiment=generate_sentiment(filename)
    #
    # entity=generate_entity(filename)

    keyword=generate_keyword(path)

    sentiment=generate_sentiment(path)

    entity=generate_entity(path)



    tempArray=[]
    for entity in entity["documents"][0]['entities']:
        tempArray.append(entity["name"])

    # print(tempArray)

    tempKeyword=[]
    for keword in keyword["documents"]:
        # for i in keword["keyPhrases"]:
        #     print(i)
            # tempArray.insert(-1,i)
        tempKeyword.extend(keword["keyPhrases"])

    # print(tempKeyword)


    d = {}



    # d["keyword"]=keyword["documents"][0]['keyPhrases']
    d["keyword"]=tempKeyword
    d["sentiment"]=sentiment["documents"][0]['score']
    d["entity"]=tempArray
    # d["entity"]=entity["documents"][0]['entities']
    d["filename"]=OrignalFileName

    print(d)


    return d

path='/home/szc/testcopy/a/case2.pdf'
# Get_keyword_sentiment_entity_dictionary("abcd.pptx")
