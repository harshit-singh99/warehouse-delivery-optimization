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



def calculate(node, weight, remaining_warehouses, reqs):
    if node == 'L1' and len(remaining_warehouses) == 0:
        return 0
    if node == 'L1':
        weight = 0
    costs = []
    for next_node in remaining_warehouses:
        w = reqs[node] + weight
        next_remaining_warehouses = [i for i in remaining_warehouses if i != next_node]
        c = cost(w, node, next_node) + calculate(next_node, w, next_remaining_warehouses, reqs)
        costs.append(c)
    if node != "L1":
        w = reqs[node] + weight
        c = cost(w, node, 'L1') + calculate('L1', w, remaining_warehouses, reqs)
        costs.append(c)
    return min(costs)
    

def cost(weight, pointA, pointB):
    distance = distance_between(pointA, pointB)
    if weight <= 5:
        return 10 * distance
    return (10 + (ceil((weight - 5)/5)) * 8) * distance

def distance_between(pointA, pointB):
    pointA = locations[pointA]
    pointB = locations[pointB]
    return distances[pointA][pointB]

def main():
    reqs = {
            "C1":4,
            "C2":10,
            "C3":0,
            "L1":0
    }
    remaining_warehouses = [key for key, val in reqs.items() if val != 0 ]
    costs = []
    for next_node in remaining_warehouses:
        w = 0
        next_remaining_warehouses = [i for i in remaining_warehouses if i != next_node]
        c = calculate(next_node, w, next_remaining_warehouses, reqs)
        costs.append(c)

    print(min(costs))

if __name__ == "__main__":
    main()