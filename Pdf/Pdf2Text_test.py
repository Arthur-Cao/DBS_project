import sys
sys.path.append(".")

import Pdf2Text as pchange



def test_basic():
    result=pchange.pdf2text("./case2.pdf")
    print (result)

if __name__ ==  "__main__":
    test_basic()
