function FiltersBar({
  activeTab,
  onTabChange,
  statusFilter,
  onStatusChange,
  doctorFilter,
  onDoctorChange,
  search,
  onSearchChange,
}) {
  const tabs = ["All", "Upcoming", "Today", "Past"];

  return (
    <div className="bg-white rounded-xl border px-4 py-3 mb-6 flex justify-between items-center">
      {/* Tabs */}
      <div className="flex gap-2">
        {tabs.map(tab => (
          <button
            key={tab}
            onClick={() => onTabChange(tab)}
            className={`px-4 py-2 rounded-md text-sm font-medium ${
              activeTab === tab
                ? "bg-blue-600 text-white"
                : "bg-gray-100 text-gray-700"
            }`}
          >
            {tab}
          </button>
        ))}
      </div>

      {/* Filters */}
      <div className="flex gap-3">
        <input
          value={search}
          onChange={(e) => onSearchChange(e.target.value)}
          placeholder="Search Appointments..."
          className="border rounded-md px-3 py-2 text-sm"
        />

        <select
          value={statusFilter}
          onChange={(e) => onStatusChange(e.target.value)}
          className="border rounded-md px-3 py-2 text-sm"
        >
          <option value="">All Status</option>
          <option value="Confirmed">Confirmed</option>
          <option value="Scheduled">Scheduled</option>
          <option value="Upcoming">Upcoming</option>
          <option value="Cancelled">Cancelled</option>
        </select>

        <select
          value={doctorFilter}
          onChange={(e) => onDoctorChange(e.target.value)}
          className="border rounded-md px-3 py-2 text-sm"
        >
          <option value="">All Doctors</option>
          <option value="Dr. A. Mehta">Dr. A. Mehta</option>
          <option value="Dr. R. Kumar">Dr. R. Kumar</option>
          <option value="Dr. S. Iyer">Dr. S. Iyer</option>
        </select>
      </div>
    </div>
  );
}

export default FiltersBar;
