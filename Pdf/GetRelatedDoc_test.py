import GetRelatedDoc as grelated


def test_basic():

    result=grelated.get_relatedDocument('case2.pdf')
    print (result)

if __name__ ==  "__main__":
    test_basic()
