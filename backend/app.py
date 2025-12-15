# app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
# import os # You can remove this import now, or keep it.

from appointment_service import (
    get_appointments,
    update_appointment_status
)

app = Flask(__name__)

# --- FINAL HARDCODE CORS FIX ---
# Replace the placeholder URL below with your EXACT VERCEL URL.
# This prevents the NoneType error in flask_cors core.py
VERCEL_LIVE_URL = "https://emr-appointment-management.vercel.app" # <--- YOUR VERCEL URL HERE

CORS(
    app,
    supports_credentials=True,
    origins=[VERCEL_LIVE_URL, "http://localhost:3000"] 
)
# -------------------------------
# -----------------------------
# Health Check
# -----------------------------
@app.errorhandler(500)
def internal_error(exception):
   app.logger.error(traceback.format_exc())
   return "Internal Server Error", 500
# -----------------------------------
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

