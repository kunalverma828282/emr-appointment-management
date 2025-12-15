# EMR Appointment Management System

A full-stack Appointment Management Dashboard built as part of the **SDE Intern Assignment**.  
The application allows users to view, filter, update, and manage patient appointments using a React frontend and a Python backend.

---

## 🚀 Live Demo

🔗 **Live Application:**  
(Replace with your deployed link)  
https://your-app-name.vercel.app

🔗 **Backend API (Local):**  
http://127.0.0.1:5000

---

## 📁 Repository Structure

emr-appointment-system/
│
├── backend/
│ ├── appointment_service.py
│ ├── app.py
│ └── venv/
│
├── frontend/
│ └── emr_frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── components/
│ │ │ ├── AppointmentCard.jsx
│ │ │ ├── SummaryCards.jsx
│ │ │ ├── FiltersBar.jsx
│ │ │ ├── CalendarWidget.jsx
│ │ │ └── Sidebar.jsx
│ │ └── main.jsx
│ └── package.json
│
└── README.md


---

## 🧠 Functional Overview

### 1️⃣ Appointment Listing
- Displays all appointments in a clean, card-based layout
- Each card includes:
  - Patient name & avatar
  - Date, time, duration
  - Appointment type & reason
  - Doctor name
  - Mode (In-Person / Video Call)
  - Phone & Email
  - Status badge with icon
  - Status update dropdown
  - Edit & Delete action icons

---

### 2️⃣ Summary Cards (Top Section)
Four summary cards provide quick insights:
- **Today’s Appointments**
- **Confirmed Appointments**
- **Upcoming Appointments**
- **Telemedicine Sessions**

These values update dynamically based on backend data.

---

### 3️⃣ Calendar Filtering
- Interactive calendar using `react-day-picker`
- Clicking a date:
  - Sets the selected date in local state
  - Fetches appointments filtered by date from backend
  - Fixes timezone bug by using `toLocaleDateString("en-CA")` instead of `toISOString()`

---

### 4️⃣ Tabs Filtering
Tabs allow quick filtering:
- **All**
- **Today**
- **Upcoming**
- **Past**

Filtering logic is based on appointment date relative to today.

---

### 5️⃣ Status Filtering
- Dropdown filter for appointment status:
  - Confirmed
  - Scheduled
  - Upcoming
  - Cancelled
- Filters are applied in combination with tabs and calendar

---

### 6️⃣ Search
- Real-time search by patient name
- Case-insensitive filtering

---

### 7️⃣ Status Update (Simulated Real-Time)
- Changing status from dropdown:
  - Calls backend `update_appointment_status`
  - Backend updates in-memory data
  - Frontend immediately refreshes appointment list

---

### 8️⃣ UI & Design
- Pixel-aligned layout based on provided mockups
- Tailwind CSS for styling
- Inter font
- Heroicons SVG icons
- Soft shadows, rounded cards, consistent spacing
- Responsive layout

---

## 🖥️ Frontend Implementation

### Main File
**`App.jsx`**  
This is the primary implementation file as required.

Key React concepts used:
- `useState` for UI state
- `useEffect` for data fetching
- Controlled filters (tabs, status, search)
- Stateless reusable components

---

## 🧩 Backend Implementation

### File: `appointment_service.py`

Contains:
- `get_appointments(date=None)`
- `update_appointment_status(appointment_id, new_status)`

Appointments are stored in an in-memory list to simulate database behavior.

### Data Consistency
- Updates mutate a single source of truth
- All fetches read from the same data structure
- Status updates are immediately reflected in frontend

---

## 🧠 GraphQL Query Design (Conceptual)

Although REST is used for implementation, the backend is designed to map cleanly to GraphQL.

### Example GraphQL Query
```graphql
query GetAppointments($date: String) {
  getAppointments(date: $date) {
    id
    name
    date
    time
    duration
    status
    doctorName
    mode
    phone
    email
    reason
    notes
  }
}

Example Mutation
mutation UpdateAppointmentStatus($id: ID!, $status: String!) {
  updateAppointmentStatus(id: $id, status: $status) {
    id
    status
  }
}

Consistency Guarantee

Single mutation entry point

No partial updates

UI always refreshes from updated data source

▶️ Running the Project Locally
Backend
cd backend
source venv/bin/activate
pip install flask flask-cors
python app.py


Backend runs on:
http://127.0.0.1:5000

Frontend
cd frontend/emr_frontend
npm install
npm run dev


Frontend runs on:
http://localhost:5173

📦 Technologies Used

Frontend: React, Vite, Tailwind CSS

Icons: Heroicons

Calendar: react-day-picker

Backend: Python, Flask

State Management: React Hooks

Styling: Tailwind utility classes

👤 Author

Kunal
SDE Intern Candidate