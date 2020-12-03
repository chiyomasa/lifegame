import sys
import numpy as np
import matplotlib.pyplot as plt

# const
N = 100
MAXT = 200

# initworld()


def initworld(world):
    chrworld = sys.stdin.readlines()

    for no, line in enumerate(chrworld):
        line = line.rstrip()
        for i in range(len(line)):
            world[no][i] = int(line[i])

# nextt()


def nextt(world):
    nextworld = [[0 for i in range(N)] for j in range(N)]
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            nextworld[i][j] = calcnext(world, i, j)

    # update world
    for i in range(N):
        for j in range(N):
            world[i][j] = nextworld[i][j]

# calcnext()


def calcnext(world, i, j):
    no_of_one = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            no_of_one += world[x][y]
    no_of_one -= world[i][j]

    # update
    if no_of_one == 3:
        return 1
    elif no_of_one == 2:
        return world[i][j]
    return 0


world = [[0 for i in range(N)] for j in range(N)]

initworld(world)
print("t=0")

# graph
w = plt.imshow(world, interpolation="nearest")

plt.pause(0.01)

for t in range(1, MAXT):
    nextt(world)
    print("t=", t)

    w.set_data(world)

    plt.pause(0.01)

plt.show()
