from math import sqrt
from random import randint

def calculate_distance(pos1, pos2):
    return sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def random_pos(width, height):
    return (
        randint(0, width-1),
        randint(0, height-1)
    )