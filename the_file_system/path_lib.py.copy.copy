import pathlib
import os.path

home = pathlib.PurePosixPath("/home/rose")
print(home)

usr_doc = home/"Documents"
print(usr_doc)
print(os.path.exists(usr_doc))
print(os.path.isdir(usr_doc))

usr_share = home/pathlib.PurePosixPath("Pictures")
print(usr_share)

usr_local = pathlib.Path("/usr/local")
share = usr_local/".."/"share"
print(share.resolve())