import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import pygal


x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 7, 8]
z = [3, 2, 4, 5, 2]
q = [2, 3, 4, 5, 6]

plt.plot(x, y, label="First line")
plt.plot(x, z, label="Second line")
plt.bar(x, y, label="bar label")
plt.stackplot(x, y, z, q, colors=['m', 'c', 'r', 'k'])
plt.scatter(x, z, label="scaterplot", color='k', marker="*")

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Number plot \nshown there")
plt.legend()
plt.legend(["s line", "t line"])
plt.show()

style.use("fivethirtyeight")
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def liveplot(i):
    graph_data = open("example.txt", "r").read()
    lines = graph_data.split("\n")
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(",")
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, liveplot, interval=1000)
plt.show()
