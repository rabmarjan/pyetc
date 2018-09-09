

import random
# let's create a linear function with some error called f
def f(x):
    res = x* 25 + 3
    error = res * random.uniform(-0.01, 0.01) # you can play with the error to see how it affects the result
    return res + error

values = []
# now using f we are going to create 300 values.
for i in range(0, 300):
    x = random.uniform(1, 1000)
    y = f(x)
    values.append((x, y))