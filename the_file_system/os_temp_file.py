import tempfile
import os
import pathlib

print("Building a filename with PID : ")
filename = "/tmp/guess_my_name.{}.txt".format(os.getpid())
print(filename)

with open(filename, "w+b") as temp:
    print("temp: ")
    print("  {!r}".format(temp))
    print("temp.name")
    print(" {!r}".format(temp.name))
os.remove(filename)

print("TemporaryFile: ")
with tempfile.TemporaryFile() as temp:
    print("temp: ")
    print("  {!r}".format(temp))
    print("temp.name")
    print("  {!r}".format(temp.name))

with tempfile.TemporaryFile() as temp:
    temp.write(b"Some data")
    temp.seek(0)
    print(temp.read())

with tempfile.TemporaryFile(mode="w+t") as temp:
    temp.writelines(["first\n", "second\n"])
    temp.seek(0)
    for line in temp:
        print(line.rstrip())

with tempfile.NamedTemporaryFile() as temp:
    print("temp: ")
    print(" {!r}".format(temp))
    print("temp.name")
    print(" {!r}".format(temp.name))
    file = pathlib.Path(temp.name)
print("Exists after close: ", file.exists())

with tempfile.SpooledTemporaryFile(max_size=100, mode="w+t", encoding="utf-8") as temp:
    print("temp {!r}".format(temp))
    for i in range(3):
        temp.write("This line reported over and over.\n")
        print(temp)

with tempfile.SpooledTemporaryFile(max_size=1000,
                                   mode='w+t',
                                   encoding='utf-8') as temp:
    print('temp: {!r}'.format(temp))

    for i in range(3):
        temp.write('This line is repeated over and over.\n')
        print(temp._rolled, temp._file)
    print('rolling over')
    temp.rollover()
    print(temp._rolled, temp._file)
