from flask import Flask, jsonify
from threading import Lock

app = Flask(__name__)
ready_to_authenticate = False
lock = Lock()

@app.route('/set-status-ok', methods=['POST'])
def set_status_ok():
    global ready_to_authenticate
    with lock:
        ready_to_authenticate = False
    return jsonify({"status": "success"}), 200
	
	
@app.route('/set-ready-to-authenticate', methods=['POST'])
def set_ready_to_authenticate():
    global ready_to_authenticate
    with lock:
        ready_to_authenticate = True
    return jsonify({"status": "success"}), 200

@app.route('/status', methods=['GET'])
def get_status():
    global ready_to_authenticate
    with lock:
        value = ready_to_authenticate
        ready_to_authenticate = False
    return jsonify({"is_ready_to_authenticate": ready_to_authenticate}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)