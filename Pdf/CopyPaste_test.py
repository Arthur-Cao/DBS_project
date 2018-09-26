import CopyPaste as cp

def test_basic():
    # to_path = "/home/szc/testcopy/a/"
    # from_path="/home/szc/from/"
    location="test"
    location1="another"
    to_path =r"C:\Findingaudit\Rawdata\dsdf"
    to_path=to_path+location
    from_path="C:\Findingaudit\\"
    cp.copypaste(from_path,to_path,"abc.pdf")
    print ("after test")

if __name__ ==  "__main__":
    test_basic()
