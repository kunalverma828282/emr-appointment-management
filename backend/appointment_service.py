# appointment_service.py

# This file simulates the data layer and business logic
# of an Appointment Scheduling & Queue Management service.

# -----------------------------
# Mock Database (Simulated Aurora/PostgreSQL)
# -----------------------------

appointments = [
  {
    "date": "2025-12-13",
    "doctorName": "Dr. A. Mehta",
    "duration": 30,
    "email": "rahul.sharma@email.com",
    "id": 1,
    "mode": "In-Person",
    "name": "Rahul Sharma",
    "notes": "Review blood sugar levels",
    "phone": "+91 98765 43210",
    "reason": "Diabetes Management",
    "status": "Confirmed",
    "time": "09:00",
    "type": "Follow-up"
  },
  {
    "date": "2025-12-14",
    "doctorName": "Dr. A. Mehta",
    "duration": 45,
    "email": "priya.verma@email.com",
    "id": 2,
    "mode": "Virtual",
    "name": "Priya Verma",
    "notes": "Routine health check",
    "phone": "+91 98765 11122",
    "reason": "Annual Physical Examination",
    "status": "Cancelled",
    "time": "10:00",
    "type": "Consultation"
  },
  {
    "date": "2025-12-15",
    "doctorName": "Dr. R. Kumar",
    "duration": 30,
    "email": "amit.singh@email.com",
    "id": 3,
    "mode": "In-Person",
    "name": "Amit Singh",
    "notes": "Pain since last 2 weeks",
    "phone": "+91 98123 45678",
    "reason": "Back Pain",
    "status": "Confirmed",
    "time": "11:00",
    "type": "Consultation"
  },
  {
    "date": "2025-12-15",
    "doctorName": "Dr. R. Kumar",
    "duration": 60,
    "email": "neha.gupta@email.com",
    "id": 4,
    "mode": "Virtual",
    "name": "Neha Gupta",
    "notes": "Fever and sore throat",
    "phone": "+91 98222 33445",
    "reason": "Cold and Flu",
    "status": "Scheduled",
    "time": "14:00",
    "type": "Consultation"
  },
  {
    "date": "2025-12-15",
    "doctorName": "Dr. S. Iyer",
    "duration": 30,
    "email": "vikas.m@email.com",
    "id": 5,
    "mode": "In-Person",
    "name": "Vikas Malhotra",
    "notes": "Healing assessment",
    "phone": "+91 99988 77665",
    "reason": "Post-surgery check",
    "status": "Confirmed",
    "time": "16:00",
    "type": "Follow-up"
  },
  {
    "date": "2025-12-16",
    "doctorName": "Dr. S. Iyer",
    "duration": 30,
    "email": "ananya.rao@email.com",
    "id": 6,
    "mode": "Virtual",
    "name": "Ananya Rao",
    "notes": "Video consultation requested",
    "phone": "+91 98877 66554",
    "reason": "Skin Rash",
    "status": "Upcoming",
    "time": "09:30",
    "type": "Telemedicine"
  },
  {
    "date": "2025-12-16",
    "doctorName": "Dr. A. Mehta",
    "duration": 30,
    "email": "sanjay.patel@email.com",
    "id": 11,
    "mode": "In-Person",
    "name": "Sanjay Patel",
    "notes": "Chest congestion evaluation",
    "phone": "+91 90011 22334",
    "reason": "Respiratory Check",
    "status": "Upcoming",
    "time": "10:30",
    "type": "Consultation"
  },
  {
    "date": "2025-12-16",
    "doctorName": "Dr. R. Kumar",
    "duration": 45,
    "email": "kavita.desai@email.com",
    "id": 12,
    "mode": "Virtual",
    "name": "Kavita Desai",
    "notes": "Review recent lab results",
    "phone": "+91 90022 33445",
    "reason": "Thyroid Follow-up",
    "status": "Upcoming",
    "time": "13:00",
    "type": "Follow-up"
  },
  {
    "date": "2025-12-16",
    "doctorName": "Dr. S. Iyer",
    "duration": 60,
    "email": "deepak.shukla@email.com",
    "id": 13,
    "mode": "In-Person",
    "name": "Deepak Shukla",
    "notes": "Pre-operative assessment",
    "phone": "+91 90033 44556",
    "reason": "Joint Pain Evaluation",
    "status": "Upcoming",
    "time": "15:00",
    "type": "Consultation"
  },
  {
    "date": "2025-12-16",
    "doctorName": "Dr. A. Mehta",
    "duration": 20,
    "email": "lata.reddy@email.com",
    "id": 14,
    "mode": "Virtual",
    "name": "Lata Reddy",
    "notes": "Quick medication check",
    "phone": "+91 90044 55667",
    "reason": "Medication Review",
    "status": "Upcoming",
    "time": "17:00",
    "type": "Telemedicine"
  },
  {
    "date": "2025-12-17",
    "doctorName": "Dr. A. Mehta",
    "duration": 20,
    "email": "rohit.jain@email.com",
    "id": 7,
    "mode": "In-Person",
    "name": "Rohit Jain",
    "notes": "High BP readings reported",
    "phone": "+91 97766 55443",
    "reason": "Blood Pressure Check",
    "status": "Upcoming",
    "time": "12:00",
    "type": "Consultation"
  },
  {
    "date": "2025-12-17",
    "doctorName": "Dr. R. Kumar",
    "duration": 30,
    "email": "praveen.nair@email.com",
    "id": 15,
    "mode": "Virtual",
    "name": "Praveen Nair",
    "notes": "Follow-up on digestion issues",
    "phone": "+91 90055 66778",
    "reason": "Gastroenterology Check",
    "status": "Upcoming",
    "time": "09:00",
    "type": "Follow-up"
  },
  {
    "date": "2025-12-17",
    "doctorName": "Dr. S. Iyer",
    "duration": 45,
    "email": "tina.shah@email.com",
    "id": 16,
    "mode": "In-Person",
    "name": "Tina Shah",
    "notes": "Initial consultation for sleep issues",
    "phone": "+91 90066 77889",
    "reason": "Insomnia",
    "status": "Upcoming",
    "time": "11:00",
    "type": "Consultation"
  },
  {
    "date": "2025-12-17",
    "doctorName": "Dr. A. Mehta",
    "duration": 60,
    "email": "manish.k@email.com",
    "id": 17,
    "mode": "Virtual",
    "name": "Manish Khanna",
    "notes": "Complex case review",
    "phone": "+91 90077 88990",
    "reason": "Chronic Fatigue Syndrome",
    "status": "Upcoming",
    "time": "14:00",
    "type": "Consultation"
  },
  {
    "date": "2025-12-17",
    "doctorName": "Dr. R. Kumar",
    "duration": 30,
    "email": "jyoti.singh@email.com",
    "id": 18,
    "mode": "In-Person",
    "name": "Jyoti Singh",
    "notes": "Regular check-up after treatment",
    "phone": "+91 90088 99001",
    "reason": "Orthopedic Follow-up",
    "status": "Upcoming",
    "time": "16:30",
    "type": "Follow-up"
  },
  {
    "date": "2025-12-18",
    "doctorName": "Dr. R. Kumar",
    "duration": 40,
    "email": "sneha.k@email.com",
    "id": 8,
    "mode": "Virtual",
    "name": "Sneha Kapoor",
    "notes": "Recurring headaches",
    "phone": "+91 96655 44332",
    "reason": "Migraine",
    "status": "Scheduled",
    "time": "10:30",
    "type": "Consultation"
  },
  {
    "date": "2025-12-18",
    "doctorName": "Dr. S. Iyer",
    "duration": 30,
    "email": "gita.s@email.com",
    "id": 19,
    "mode": "In-Person",
    "name": "Gita Sharma",
    "notes": "New patient assessment",
    "phone": "+91 90099 00112",
    "reason": "Initial Screening",
    "status": "Scheduled",
    "time": "14:30",
    "type": "Consultation"
  },
  {
    "date": "2025-12-18",
    "doctorName": "Dr. A. Mehta",
    "duration": 30,
    "email": "harish.v@email.com",
    "id": 20,
    "mode": "Virtual",
    "name": "Harish Varma",
    "notes": "Routine check for cholesterol",
    "phone": "+91 90110 01122",
    "reason": "Cardiology Review",
    "status": "Scheduled",
    "time": "16:00",
    "type": "Telemedicine"
  },
  {
    "date": "2025-12-19",
    "doctorName": "Dr. S. Iyer",
    "duration": 30,
    "email": "arjun.nair@email.com",
    "id": 9,
    "mode": "In-Person",
    "name": "Arjun Nair",
    "notes": "Sports injury follow-up",
    "phone": "+91 95544 33221",
    "reason": "Knee Pain",
    "status": "Upcoming",
    "time": "11:30",
    "type": "Consultation"
  },
  {
    "date": "2025-12-19",
    "doctorName": "Dr. R. Kumar",
    "duration": 45,
    "email": "rita.p@email.com",
    "id": 21,
    "mode": "Virtual",
    "name": "Rita Prakash",
    "notes": "Mental health check-in",
    "phone": "+91 90121 12233",
    "reason": "Stress Management",
    "status": "Scheduled",
    "time": "13:30",
    "type": "Consultation"
  },
  {
    "date": "2025-12-19",
    "doctorName": "Dr. A. Mehta",
    "duration": 60,
    "email": "vijay.b@email.com",
    "id": 22,
    "mode": "In-Person",
    "name": "Vijay Bhargav",
    "notes": "Complete medical history review",
    "phone": "+91 90132 23344",
    "reason": "Wellness Consultation",
    "status": "Confirmed",
    "time": "15:30",
    "type": "Consultation"
  },
  {
    "date": "2025-12-20",
    "doctorName": "Dr. A. Mehta",
    "duration": 45,
    "email": "pooja.m@email.com",
    "id": 10,
    "mode": "Virtual",
    "name": "Pooja Mishra",
    "notes": "Requested confidential video session",
    "phone": "+91 94433 22110",
    "reason": "Anxiety Consultation",
    "status": "Upcoming",
    "time": "13:00",
    "type": "Telemedicine"
  },
  {
    "date": "2025-12-20",
    "doctorName": "Dr. S. Iyer",
    "duration": 30,
    "email": "chandan.k@email.com",
    "id": 23,
    "mode": "In-Person",
    "name": "Chandan Kadam",
    "notes": "Referred by Dr. Shah",
    "phone": "+91 90143 34455",
    "reason": "Dermatology Check",
    "status": "Scheduled",
    "time": "10:00",
    "type": "Consultation"
  },
  {
    "date": "2025-12-20",
    "doctorName": "Dr. R. Kumar",
    "duration": 30,
    "email": "preeti.j@email.com",
    "id": 24,
    "mode": "Virtual",
    "name": "Preeti Jha",
    "notes": "Quick question on dosage",
    "phone": "+91 90154 45566",
    "reason": "Medication Follow-up",
    "status": "Upcoming",
    "time": "16:00",
    "type": "Follow-up"
  },
  {
    "date": "2025-12-21",
    "doctorName": "Dr. A. Mehta",
    "duration": 40,
    "email": "rahul.b@email.com",
    "id": 25,
    "mode": "In-Person",
    "name": "Rahul Bose",
    "notes": "Annual physical booked",
    "phone": "+91 90165 56677",
    "reason": "Annual Physical Examination",
    "status": "Scheduled",
    "time": "09:00",
    "type": "Consultation"
  },
  {
    "date": "2025-12-21",
    "doctorName": "Dr. R. Kumar",
    "duration": 30,
    "email": "samina.a@email.com",
    "id": 26,
    "mode": "Virtual",
    "name": "Samina Ali",
    "notes": "Routine check-up",
    "phone": "+91 90176 67788",
    "reason": "General Check-up",
    "status": "Upcoming",
    "time": "11:00",
    "type": "Telemedicine"
  },
  {
    "date": "2025-12-22",
    "doctorName": "Dr. S. Iyer",
    "duration": 60,
    "email": "aakash.g@email.com",
    "id": 27,
    "mode": "In-Person",
    "name": "Aakash Goel",
    "notes": "Initial consultation for stomach pain",
    "phone": "+91 90187 78899",
    "reason": "Abdominal Pain",
    "status": "Scheduled",
    "time": "14:00",
    "type": "Consultation"
  },
  {
    "date": "2025-12-22",
    "doctorName": "Dr. A. Mehta",
    "duration": 30,
    "email": "dipti.r@email.com",
    "id": 28,
    "mode": "Virtual",
    "name": "Dipti Rawat",
    "notes": "Check on recent medication change",
    "phone": "+91 90198 89001",
    "reason": "Hypertension Review",
    "status": "Upcoming",
    "time": "17:30",
    "type": "Follow-up"
  },
  {
    "date": "2025-12-23",
    "doctorName": "Dr. R. Kumar",
    "duration": 45,
    "email": "nandini.s@email.com",
    "id": 29,
    "mode": "In-Person",
    "name": "Nandini Singh",
    "notes": "Follow up after minor procedure",
    "phone": "+91 90209 90112",
    "reason": "Wound Check",
    "status": "Confirmed",
    "time": "10:30",
    "type": "Follow-up"
  },
  {
    "date": "2025-12-23",
    "doctorName": "Dr. S. Iyer",
    "duration": 30,
    "email": "kartik.m@email.com",
    "id": 30,
    "mode": "Virtual",
    "name": "Kartik Menon",
    "notes": "Requested evening virtual session",
    "phone": "+91 90220 01223",
    "reason": "Allergy Consultation",
    "status": "Scheduled",
    "time": "18:00",
    "type": "Telemedicine"
  }
]


# -----------------------------
# Query Function
# -----------------------------

def get_appointments(filters=None):
    """
    Simulates a GraphQL query to fetch appointments.

    filters (dict):
        - date (str): 'YYYY-MM-DD'
        - status (str): 'Confirmed', 'Scheduled', etc.

    Returns:
        List of filtered appointments
    """

    # Start with all appointments
    result = appointments

    if filters:
        # Filter by date if provided
        if "date" in filters and filters["date"]:
            result = [
                appt for appt in result
                if appt["date"] == filters["date"]
            ]

        # Filter by status if provided
        if "status" in filters and filters["status"]:
            result = [
                appt for appt in result
                if appt["status"] == filters["status"]
            ]

    return result
# -----------------------------
# Mutation Function
# -----------------------------

def update_appointment_status(appointment_id, new_status):
    """
    Simulates a GraphQL mutation to update appointment status.

    In a real system:
    - This would perform a transactional write to Aurora/PostgreSQL
    - AppSync would then trigger a Subscription event
      to notify all connected frontend clients in real time
    """

    for appointment in appointments:
        if appointment["id"] == appointment_id:
            appointment["status"] = new_status

            # In real architecture:
            # 1. Write change to Aurora DB (transactional)
            # 2. AppSync publishes subscription update
            # 3. Frontend receives real-time update

            return appointment

    # If appointment not found
    return None
