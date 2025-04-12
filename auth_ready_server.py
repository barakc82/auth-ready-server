from flask import Flask, jsonify
from threading import Lock

app = Flask(__name__)
ready_to_authenticate = False
lock = Lock()

@app.route('/set', methods=['GET'])
def set_ready():
    global ready_to_authenticate
    with lock:
        ready_to_authenticate = True
    return jsonify({"status": "ready", "value": True})

@app.route('/get', methods=['GET'])
def get_ready():
    global ready_to_authenticate
    with lock:
        value = ready_to_authenticate
        ready_to_authenticate = False  # reset after reading, optional
    return jsonify({"value": value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)