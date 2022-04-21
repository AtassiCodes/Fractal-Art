import random
import time
from turtle import *

speed(-1000)
start_time = time.time()

bgcolor("black")
color("white")


pensize(1)
# r, g, b = random.rand(0.0, 255.0), random.randint(0.0, 255.0), random.randint(0.0, 255.0)
# pencolor((r, g, b))

def tree(size, levels, angle):
    if levels == 0:
        return
    forward(size)
    right(angle)

    tree(size * 0.8, levels - 1, angle)

    left(angle * 2)

    tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)

    tree(size * 0.8, levels - 1, angle)


left(45)
tree(125, 8, 45)

print("--- %s seconds ---" % (time.time() - start_time))
mainloop()
