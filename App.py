from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def dafault_route():
    return f"EzhBattle2_0_back"

@app.route("/get_value")
def get_value():
    return f"{progress}", 200

@app.route("/up_value")
def up_value():
    global progress
    progress+=0.01
    return f"{progress}", 200

@app.route("/down_value")
def down_value():
    global progress
    progress-=0.01
    return f"{progress}", 200

if __name__ == '__main__':
    global progress
    progress = 0
    app.run(host='0.0.0.0')
    # app.run()