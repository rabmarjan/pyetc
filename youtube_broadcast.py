from itertools import combinations_with_replacement as pc

n = list(map(str, input().split()))
for i, j in pc(n[0], int(n[1])):
    s = ""
    x = "{0}{1}".format(i, j)
    print(x)
