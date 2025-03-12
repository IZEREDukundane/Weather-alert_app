from flask import request, jsonify
from firebase_config import db

@app.route("/set_preferences", methods=["POST"])
def set_preferences():
    # Get user preferences from the request
    user_id = request.json.get('user_id')
    location = request.json.get('location')
    alert_type = request.json.get('alert_type')  # E.g., rain, storm, temperature
    frequency = request.json.get('frequency')    # How often they want notifications

    # Store user preferences in Firestore
    user_ref = db.collection('users').document(user_id)
    user_ref.set({
        'location': location,
        'alert_type': alert_type,
        'frequency': frequency
    })

    return jsonify({"message": "Preferences saved successfully!"}), 200

