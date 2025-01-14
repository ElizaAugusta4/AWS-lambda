from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Flask API on AWS Lambda!"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

if __name__ != "__main__":
    # AWS Lambda handler
    from awslambdaric.lambda_handler import handler
