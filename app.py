from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

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
    r = request.data
    r = json.loads(r)
    print(r)
    return jsonify(r)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port='8000')
