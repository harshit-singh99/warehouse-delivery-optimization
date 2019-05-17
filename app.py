from flask import Flask, jsonify, request, abort
import json
from math import ceil

app = Flask(__name__)

weights = {
            "A": 3,
            "B": 2,
            "C": 8,
            "D": 12,
            "E": 25,
            "F": 15,
            "G": 0.5,
            "H": 1,
            "I": 2,
            }

stored_at = {
            "A": "C1",
            "B": "C1",
            "C": "C1",
            "D": "C2",
            "E": "C2",
            "F": "C2",
            "G": "C3",
            "H": "C3",
            "I": "C3",
            }

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
    if node == "L1" and len(remaining_warehouses) == 0:
        return 0
    if node == "L1":
        weight = 0
    costs = []
    for next_node in remaining_warehouses:
        w = reqs[node] + weight
        next_remaining_warehouses = [i for i in remaining_warehouses if i != next_node]
        c = cost(w, node, next_node) + calculate(next_node, w, next_remaining_warehouses, reqs)
        costs.append(c)
    if node != "L1":
        w = reqs[node] + weight
        c = cost(w, node, "L1") + calculate("L1", w, remaining_warehouses, reqs)
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


@app.route('/', methods=['GET'])
def index():
    st =  {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
            "F": 0,
            "G": 0,
            "H": 0,
            "I": 0,
            }
    return jsonify(st)

@app.route('/', methods=['POST'])
def do():
    #print(request.content)
    #if not request.json:
    #    abort(400)
    reqs = {
            "C1":0,
            "C2":0,
            "C3":0,
            "L1":0
    }
    try:
        r = request.data
        r = json.loads(r)
        for key, val in r.items():
            reqs[stored_at[key]] += float(val) * weights[key]
    except:
        abort(400)

    remaining_warehouses = [key for key, val in reqs.items() if val != 0 ]
    costs = []
    for next_node in remaining_warehouses:
        w = 0
        next_remaining_warehouses = [i for i in remaining_warehouses if i != next_node]
        c = calculate(next_node, w, next_remaining_warehouses, reqs)
        costs.append(c)
    try:
        final = min(costs)
    except:
        final = 0

    return jsonify({"min-cost": final})

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port='8000')
