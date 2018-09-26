import operations as op
import mongodb_client as client

def test_basic():
    # op.UploadDocument("DocumentNameaaddvedfd","Location","MeetingType","Year","Month","Author","KeyWords","Entities","sensitive")
    db = client.get_db('CLICK_LOGS_TABLE_NAME')

    # op.GetDocumentBySearch("danial","[HO]Singapore","Low", "[CM]Country Reports")
    # op.GetDocumentBySearch("","","","")
    #1 word
    # op.GetDocumentBySearch("danial","Location", "Low", "[CM]SME Portfolio Reports","Planet Karaoke Pub project")
    op.GetDocumentBySearch(None,None,None,None,"")
    # op.GetDocumentBySea   rch("","","", "","project")
    # op.GetDocumentBySearch("","","Low", "")
    # op.GetDocumentBySearch("","","", "[CM]Country Reports")
    #2 words
    # op.GetDocumentBySearch("danial","[HO]Singapore","", "")
    # op.GetDocumentBySearch("danial","","Low", "")
    # op.GetDocumentBySearch("danial","","", "[CM]Country Reports")
    # op.GetDocumentBySearch("","[HO]Singapore","Low", "")
    # op.GetDocumentBySearch("","[HO]Singapore","", "[CM]Country Reports")
    # op.GetDocumentBySearch("","","Low", "[CM]Country Reports")


    print ('test_basic passed!')

if __name__ ==  "__main__":
    test_basic()
