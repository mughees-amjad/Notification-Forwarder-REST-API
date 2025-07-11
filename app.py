# app.py
from flask import Flask, request, jsonify
from messenger import send_to_telegram

app = Flask(__name__)

notifications = []  # In-memory storage

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()

    # Basic validation
    if not data or 'Type' not in data or 'Name' not in data or 'Description' not in data:
        return jsonify({"error": "Invalid notification format"}), 400

    notifications.append(data)

    if data["Type"] == "Warning":
        success = send_to_telegram(data)
        if success:
            return jsonify({"message": "Notification forwarded"}), 200
        else:
            return jsonify({"error": "Failed to forward message"}), 500
    else:
        return jsonify({"message": "Info notification ignored"}), 200

@app.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify(notifications)
