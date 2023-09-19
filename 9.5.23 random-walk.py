import random
import matplotlib.pyplot as plt

steps = int(input("please choose amount of steps of steps"))
dimensions = int(input("please choose number of possible dimensions"))

coordinate_system = [[0 for steps in range(steps + 1)] for dim in range(dimensions + 1)]

def move(dimensions, steps):
    direction = 1
    choosen_dimension = random.randint(0, dimensions)
    coin_flip = random.random()
    if coin_flip < 0.5:
        direction = -1
[def move(dimensions, steps):] for coordinate_system in