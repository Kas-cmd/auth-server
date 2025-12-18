from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# -----------------------------
# ✅ Authorized Serial Numbers
# Add new serials here as strings, separated by commas
# Example: "NEW001", "NEW002"
# Keep the quotes around each serial
# -----------------------------
AUTHORIZED = [
    "ABC123",
    "DEF456",
    "GHI789"
]

@app.route("/check", methods=["POST"])
def check():
    """
    Endpoint to check if a device serial number is authorized.
    Expects JSON like: {"serial": "ABC123"}
    Returns: {"authorized": True} or {"authorized": False}
    """
    serial = request.json.get("serial")
    if serial is None:
        return jsonify({"authorized": False, "error": "No serial provided"}), 400

    is_authorized = serial in AUTHORIZED
    return jsonify({"authorized": is_authorized})

# -----------------------------
# Required for Render: bind to the port Render provides
# -----------------------------
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
