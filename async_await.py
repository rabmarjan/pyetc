import asyncio
from time import sleep
import datetime


async def hello_world():
    print("Hello World!")


# Blocking call which returns when the hello_world() coroutine is done
# loop.run_until_complete(hello_world())
# loop.close()


def hello():
    print("Hello")
    sleep(3)
    print("world")


@asyncio.coroutine
def hello1():
    print("hello from hello1")
    yield from asyncio.sleep(2)
    print("world from hello1")


async def hello2():
    print("Hello from hello2")
    await asyncio.sleep(2)
    print("world from hello2")


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


################################################
async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result("Future is done")


loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
loop.run_until_complete(future)
print(future.result())
################################################
async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

def got_result(future):
    print(future.result())
    loop.stop()

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
future.add_done_callback(got_result)
try:
    loop.run_forever()
finally:
    pass
    #loop.close()
###############################################
async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    factorial("A", 2),
    factorial("B", 3),
    factorial("C", 4),
))
#loop.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello1())
    loop.run_until_complete(hello2())
    loop.run_until_complete(print_sum(1, 2))
    loop.close()
