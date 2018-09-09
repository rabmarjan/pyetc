import shutil
import glob
import os
print("Before: ", glob.glob("path_lib.*"))
shutil.copyfile("path_lib.py", "path_lib.py.copy")
shutil.copy("path_lib.py", "path_lib.py.copy.copy")
print("After: ", glob.glob("path_lib.*"))

stat_info = os.stat("path_lib.py")
print(stat_info.st_atime)