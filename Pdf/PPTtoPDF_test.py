import PPTtoPDF as Topdf


def test_basic():

    Topdf.PPTtoPDF("abc.pptx","topdf.pdf")

    print ('test_basic passed!')

if __name__ ==  "__main__":
    test_basic()
