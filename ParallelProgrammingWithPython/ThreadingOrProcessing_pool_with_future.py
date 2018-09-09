from concurrent import futures
import threading
import multiprocessing
import random
import time


# example ref
# https://pymotw.com/3/concurrent.futures/index.html#scheduling-individual-tasks

def task10(n):
    print("{}: sleeping {}".format(threading.current_thread().name, n))
    time.sleep(n / 10)
    print("{}: done with {}".format(threading.current_thread().name, n))
    return n / 10


ex = futures.ThreadPoolExecutor(max_workers=2)
print("main: starting")
results = ex.map(task10, range(5, 0, -1))
print("main: unprocessed results {}".format(results))
print("main: waiting for real results")
real_results = list(results)
print("main: results: {}".format(real_results))


def task11(n):
    print("{}: sleeping {}".format(threading.current_thread().name, n))
    time.sleep(n / 10)
    print("{}: done with {}".format(threading.current_thread().name, n))
    return n / 10


exs = futures.ThreadPoolExecutor(max_workers=2)
print("main: starting")
f = exs.submit(task11, 5)
print("main: future: {}".format(f))
print("main: waiting for results")
result = f.result()
print("main: result: {}".format(result))
print("main: future after result:{}".format(f))


def task12(n):
    time.sleep(random.random())
    return (n, n / 10)


exg = futures.ThreadPoolExecutor(max_workers=5)
print('main: starting')

wait_for = [
    exg.submit(task12, i)
    for i in range(5, 0, -1)
]

for f in futures.as_completed(wait_for):
    print('main: result: {}'.format(f.result()))


def task1(num_list):
    # num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in num_list:
        print("Print num squere ", num * num)


def task2(num_list):
    # num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in num_list:
        print("Print num quebe", num * num * num)


with futures.ThreadPoolExecutor(max_workers=2) as ex:
    num_list = [1, 2, 3, 4]
    print('main: starting')
    ex.submit(task1, num_list)
    ex.submit(task1, num_list)
    ex.submit(task2, num_list)
    ex.submit(task2, num_list)

print('main: done')

# l = ["A", "B", "C"]
# m = ["Apple", "Bannana", "Candy"]
# counter = 0
# while counter < len(l):
#     x = l[counter]
#     y = m[counter]
#     print(x, ": ", y)
#     counter += 1
