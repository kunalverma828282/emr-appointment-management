import { useEffect, useState } from "react";
import Sidebar from "./components/Sidebar";
import SummaryCards from "./components/SummaryCards";
import FiltersBar from "./components/FiltersBar";
import AppointmentCard from "./components/AppointmentCard";
import CalendarWidget from "./components/CalendarWidget";

function App() {
  const [appointments, setAppointments] = useState([]);
  const [filteredAppointments, setFilteredAppointments] = useState([]);
  const [activeTab, setActiveTab] = useState("All");
  const [selectedDate, setSelectedDate] = useState("");
  const [statusFilter, setStatusFilter] = useState("");
  const [doctorFilter, setDoctorFilter] = useState("");
  const [search, setSearch] = useState("");

  /* ---------------- FETCH DATA ---------------- */
  useEffect(() => {
    fetchAppointments();
  }, []);

  const fetchAppointments = (date = "") => {
    let url = "http://127.0.0.1:5000/appointments";
    if (date) url += `?date=${date}`;

    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        setAppointments(data);
        applyFilters(activeTab, data, statusFilter, doctorFilter, search);
      });
  };

  /* ---------------- FILTER LOGIC ---------------- */
  const applyFilters = (
    tab,
    data = appointments,
    status = statusFilter,
    doctor = doctorFilter,
    searchText = search
  ) => {
    const today = new Date().toLocaleDateString("en-CA");
    let result = [...data];

    // Tabs
    if (tab === "Today") result = result.filter(a => a.date === today);
    else if (tab === "Upcoming") result = result.filter(a => a.date > today);
    else if (tab === "Past") result = result.filter(a => a.date < today);

    // Status
    if (status) result = result.filter(a => a.status === status);

    // Doctor
    if (doctor) result = result.filter(a => a.doctorName === doctor);

    // Search
    if (searchText) {
      result = result.filter(a =>
        a.name.toLowerCase().includes(searchText.toLowerCase())
      );
    }

    setActiveTab(tab);
    setFilteredAppointments(result);
  };

  /* ---------------- STATUS UPDATE ---------------- */
  const updateStatus = (id, status) => {
    fetch(`http://127.0.0.1:5000/appointments/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status }),
    }).then(() => fetchAppointments(selectedDate));
  };

  /* ---------------- UI ---------------- */
  return (
    <div className="min-h-screen bg-[#f6f8fb] flex">
      {/* SIDEBAR */}
      <Sidebar />

      {/* MAIN */}
      <main className="flex-1 px-8 py-6 max-w-[1400px] mx-auto">
        {/* Header */}
        <div className="flex justify-between items-center mb-6">
          <div>
            <h1 className="text-2xl font-semibold text-gray-900">
              Appointment Management
            </h1>
            <p className="text-sm text-gray-500">
              Schedule and manage patient appointments
            </p>
          </div>

          <div className="flex gap-3">
            <button className="border px-4 py-2 rounded-md bg-white text-sm">
              ⬇ Export
            </button>
            <button className="bg-blue-600 text-white px-4 py-2 rounded-md text-sm">
              + New Appointment
            </button>
          </div>
        </div>

        {/* Summary Cards */}
        <SummaryCards appointments={appointments} />

        {/* Filters */}
        <FiltersBar
          activeTab={activeTab}
          onTabChange={(tab) =>
            applyFilters(tab, appointments, statusFilter, doctorFilter, search)
          }
          statusFilter={statusFilter}
          onStatusChange={(s) => {
            setStatusFilter(s);
            applyFilters(activeTab, appointments, s, doctorFilter, search);
          }}
          doctorFilter={doctorFilter}
          onDoctorChange={(d) => {
            setDoctorFilter(d);
            applyFilters(activeTab, appointments, statusFilter, d, search);
          }}
          search={search}
          onSearchChange={(v) => {
            setSearch(v);
            applyFilters(activeTab, appointments, statusFilter, doctorFilter, v);
          }}
        />

        {/* CONTENT GRID */}
        <div className="grid grid-cols-[320px_1fr] gap-6 items-start">
          {/* Calendar */}
          <CalendarWidget
            selectedDate={selectedDate}
            onDateChange={(date) => {
              setSelectedDate(date);
              fetchAppointments(date);
            }}
          />

          {/* Appointments */}
          <div className="space-y-4">
            {filteredAppointments.map((appt) => (
              <AppointmentCard
                key={appt.id}
                appt={appt}
                onStatusChange={updateStatus}
              />
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
