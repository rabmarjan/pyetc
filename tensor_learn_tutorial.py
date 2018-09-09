# import numpy as np
# import cv2


# img = cv2.imread("/home/rose/Pictures/MyPic.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter("/home/rose/Pictures/openCVVideoOutput.avi", fourcc, 20.0, (640, 480))

# while True:
#     res, frame = cap.read()
#     rgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     ray = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
#     cv2.imshow("frame", frame)
#     cv2.imshow("gray", rgray)
#     #cv2.imshow("ray", ray)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# cap.release()
# #out.release()
# cv2.destroyAllWindows()


# import time
# import asyncio
#
# def sumOfN(n):
#     start = time.time()
#
#     theSum = 0
#     for i in range(1, n + 1):
#         theSum = theSum + i
#
#     end = time.time()
#
#     return theSum, end - start
#
#
# for i in range(5):
#     print("Sum is %d required %f  seconds"%sumOfN(10000))
# print("+++++++++++++++++++")
# def sum_of_n2(n):
#     start = time.time()
#     x = (n*(n+1))/2
#     end = time.time()
#     return x, end-start
#
# for j in range(5):
#     print("Sum of the result %d got seconds %f"%sum_of_n2(10000000000000000000))
#
# def orderedSequentialSearch(alist, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(alist) and not found and not stop:
#         if alist[pos] == item:
#             found = True
#         else:
#             if alist[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#
#     return found

#
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
# print(orderedSequentialSearch(testlist, 3))
# print(orderedSequentialSearch(testlist, 13))
import timeit
from timeit import Timer


def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


print(listsum([1, 3, 5, 7, 9]))

def listsum1(numList):
    acco = 0
    for i in numList:
        acco += i
    return acco

print(listsum1([1,3,5,7,9]))


x = Timer("listsum([1,3,5,7,9])", "from __main__ import listsum")
y = Timer("listsum1([1,3,5,7,9])", "from __main__ import listsum1")
print("The sum is from recurtion: ", x.timeit(number=100000), "miliseconds")
print("The sum is from loop: ", y.timeit(number=100000), "miliseconds")


