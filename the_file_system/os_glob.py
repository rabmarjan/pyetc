import glob
import os
import fnmatch
import pprint

for name in sorted(glob.glob("../*.html")):
    print(os.path.abspath(name))

pattern = "os_*.py"

files = os.listdir(".")
for file in files:
    print("Filename: {:<25} {}".format(file, fnmatch.fnmatch(file, pattern)))
    print("=====================")
    print("Filename Match Case: {:<25} {}".format(file, fnmatch.fnmatchcase(file, pattern)))

print("\nFiles : ")
pprint.pprint(files, depth=4)
print("\nMatcches : ")
pprint.pprint(fnmatch.filter(files, pattern))
