# def netwon_sqrt(n):
#     root = n / 2
#     for i in range(15):
#         root = (1 / 2) * (root + (n / root))
#     return root

import threading
import multiprocessing
import time
import timeit
from timeit import Timer

process_lock = multiprocessing.Lock()


# result = []


def multy1(num, result):
    #   global result
    for id, val in enumerate(num):
        time.sleep(0.2)
        process_lock.acquire()
        result[id] = val * val
        print("Print Squre ", val * val)
        process_lock.release()


def calc_square(numbers, q):
    for n in numbers:
        q.put(n * n)


def multy2(num):
    for i in num:
        time.sleep(0.2)
        process_lock.acquire()
        print("Print Qube ", i * i * i)
        process_lock.release()


if __name__ == "__main__":
    # print(netwon_sqrt(25))
    # n = 1000
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # thread1 = threading.Thread(target=multy1, args=(num,))
    # thread2 = threading.Thread(target=multy2, args=(num,))
    result = multiprocessing.Array('i', 10)
    q = multiprocessing.Queue()
    process1 = multiprocessing.Process(target=multy1, args=(num, result))
    process2 = multiprocessing.Process(target=multy2, args=(num,))
    p = multiprocessing.Process(target=calc_square, args=(num, q))
    start = time.time()
    # thread1.start()
    # thread2.start()
    #
    # thread1.join()
    # thread2.join()
    # print(multy1(num))
    # print(multy2(num))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    p.start()
    p.join()
    while q.empty() is False:
        print(q.get(), end=" ")
    end = time.time()
    print("\nTimes taken ", str(end - start), "seconds")
    print(result[:])
    # print(sum1(n))
    # print(sum2(n))
    # print("Function take total " + str(time.time() - start) + "seconds")
    # t1 = Timer("sum1(100)", "from __main__ import sum1")
    # t2 = Timer("sum2(100)", "from __main__ import sum2")
    # print("Time taken", t1.timeit(number=1000) + t2.timeit(number=1000), "miliseconds")
    # print("Time taken", t2.timeit(number=1000), "miliseconds")
