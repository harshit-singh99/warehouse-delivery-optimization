from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'A': 7, 'B':90})

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port='8000')
