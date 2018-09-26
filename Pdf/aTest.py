import os


def test_basic():
    filename, file_extension = os.path.splitext('somefile.ext')
    # result=grelated.get_relatedDocument('case2.pdf')
    print (file_extension)
    print(filename)

if __name__ ==  "__main__":
    test_basic()
