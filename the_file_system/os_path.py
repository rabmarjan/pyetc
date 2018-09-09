import os.path
import time

PATHS = [
    "/one/two/three",
    "/one/two/three/",
    "/",
    ".",
    "",
]

for path in PATHS:
    print("{!r:>17} : {}".format(path, os.path.split(path)))

for path in PATHS:
    print("{!r:>17} : {!r}".format(path, os.path.basename(path)))

PATHS = [
    'filename.txt',
    'filename',
    '/path/to/filename.txt',
    '/',
    '',
    'my-archive.tar.gz',
    'no-extension.',
]

for path in PATHS:
    print("{!r:>21} : {!r}".format(path, os.path.splitext(path)))

PATHS = [("one", "two", "three"),
         ("/", "one", "two", "three"),
         ("/one", "/two", "/three"),
         ]
for parts in PATHS:
    print("{0} : {1}".format(parts, os.path.join(*parts)))

print("File : ", __file__)
print("Access time : ", time.ctime(os.path.getatime(__file__)))
print("Modified time : ", time.ctime(os.path.getmtime(__file__)))
print("Change time : ", time.ctime(os.path.getctime(__file__)))
print("Size : ", os.path.getsize(__file__))

FILENAMES = [
    __file__,
    os.path.dirname(__file__),
    "/",
    "./broken_link",
]

for file in FILENAMES:
    print("File : ".format(file))
    print("Absolute : {}".format(os.path.isabs(file)))
    print("Is File? : {}".format(os.path.isfile(file)))
    print("Is Dir? : {}".format(os.path.isdir(file)))
    print("Is Link : {}".format(os.path.islink(file)))
    print("Mountpoint? : {}".format(os.path.ismount(file)))
    print("Exists? : {}".format(os.path.exists(file)))
    print("Link Exists? : {}".format(os.path.lexists(file)))
    print()

