import KeywordStoreInDatabase as Keystore

def test_basic():
    # db = client.get_db('test')
    # db.demo.drop()
    # assert db.demo.count() == 0
    # db.demo.insert({'test':123})
    # assert db.demo.count() == 1
    # db.demo.drop()
    # assert db.demo.count() == 0
    Keystore.UploadDocument("case2.pdf","[CM]China","[CM]SME Portfolio Reports","Year","Month","ImportantLevel","danial","case2.pdf","Low")
    # Keystore.UploadDocument("case study.pdf","Location","[CM]SME Portfolio Reports","Year","Month","ImportantLevel","danial","case study.pdf","Low")
    # Keystore.UploadDocument("abc.pdf","Location","[CM]SME Portfolio Reports","Year","Month","ImportantLevel","danial","abc.pdf","Low")

    print ('test_basic passed!')

if __name__ ==  "__main__":
    test_basic()
