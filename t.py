from math import ceil
locations = {
            "C1": 0,
            "C2": 1,
            "C3": 2,
            "L1": 3
            }

distances = [[0, 4, 5, 3],
            [4, 0, 3, 2.5],
            [5, 3, 0, 2],
            [3, 2.5, 2, 0]]

def cost(weight, distance):
    if weight <= 5:
        return 10 * distance
    return (10 + (ceil((weight - 5)/5)) * 8) * distance

def distance_between(pointA, pointB):
    pointA = locations[pointA]
    pointB = locations[pointB]
    return distances[pointA][pointB]

