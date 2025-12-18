from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# List of authorized serial numbers
AUTHORIZED = ["ABC123", "DEF456", "GHI789"]

@app.route("/check", methods=["POST"])
def check():
    serial = request.json.get("serial")
    return jsonify({"authorized": serial in AUTHORIZED})

# Render requires this to choose the port
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
