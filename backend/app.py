# app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from appointment_service import (
    get_appointments,
    update_appointment_status
)

app = Flask(__name__)
# --- CORS Configuration ---
# Get the deployed Vercel URL from the environment variable.
# Fallback to localhost is only used if the env var is completely missing.
VERCEL_ORIGIN = os.environ.get("https://emr-appointment-management.vercel.app/")

# Define the origins that are allowed. 
# We add both Vercel URL (if it exists) and the localhost fallback.
allowed_origins = ["http://localhost:3000"]
if VERCEL_ORIGIN:
    allowed_origins.append(VERCEL_ORIGIN)

CORS(app, supports_credentials=True, origins=allowed_origins) 
# --------------------------
# Configure CORS to explicitly allow requests ONLY from your Vercel URL
CORS(app, supports_credentials=True, origins=[VERCEL_ORIGIN])
# -----------------------------
# Health Check
# -----------------------------

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "Backend is running"})


# -----------------------------
# Get Appointments (Query)
# -----------------------------

@app.route("/appointments", methods=["GET"])
def fetch_appointments():
    """
    Query parameters:
    - date
    - status
    Example:
    /appointments?date=2025-11-06&status=Confirmed
    """

    date = request.args.get("date")
    status = request.args.get("status")

    filters = {}

    if date:
        filters["date"] = date
    if status:
        filters["status"] = status

    appointments = get_appointments(filters if filters else None)

    return jsonify(appointments)


# -----------------------------
# Update Appointment Status (Mutation)
# -----------------------------

@app.route("/appointments/<int:appointment_id>", methods=["PUT"])
def update_status(appointment_id):
    """
    JSON Body:
    {
        "status": "Confirmed"
    }
    """

    data = request.get_json()
    new_status = data.get("status")

    updated_appointment = update_appointment_status(
        appointment_id, new_status
    )

    if not updated_appointment:
        return jsonify({"error": "Appointment not found"}), 404

    return jsonify(updated_appointment)


# -----------------------------
# Start Server
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)

