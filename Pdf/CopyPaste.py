import shutil
import os

def copypaste(from_path,to_path,filename):
    path = "/home/szc/testcopy/a"
    if (os.path.isdir(to_path))==False:
        os.mkdir(to_path)
    # print(os.path.isdir(path))
    shutil.copy2(from_path+filename, to_path) # complete target filename given
    return "Success"
    # shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext
