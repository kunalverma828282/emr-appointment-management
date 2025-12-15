import {
  CalendarDaysIcon,
  CheckCircleIcon,
  ClockIcon,
  VideoCameraIcon,
} from "@heroicons/react/24/outline";

function SummaryCards({ appointments = [] }) {
  const today = new Date().toLocaleDateString("en-CA");

  const todayCount = appointments.filter(a => a.date === today).length;
  const confirmedCount = appointments.filter(a => a.status === "Confirmed").length;
  const upcomingCount = appointments.filter(a => a.date > today).length;
  const telemedicineCount = appointments.filter(a => a.mode === "Virtual").length;

  const cards = [
    { label: "Today", value: todayCount, icon: CalendarDaysIcon, color: "text-blue-600 bg-blue-50" },
    { label: "Confirmed", value: confirmedCount, icon: CheckCircleIcon, color: "text-green-600 bg-green-50" },
    { label: "Upcoming", value: upcomingCount, icon: ClockIcon, color: "text-indigo-600 bg-indigo-50" },
    { label: "Telemedicine", value: telemedicineCount, icon: VideoCameraIcon, color: "text-purple-600 bg-purple-50" },
  ];
  

  return (
    <div className="grid grid-cols-4 gap-6 mb-8">
      {cards.map(({ label, value, icon: Icon, color }) => (
        <div
          key={label}
          className="bg-white rounded-2xl border shadow-[0_8px_24px_rgba(0,0,0,0.06)] px-6 py-5 flex items-center gap-4"
        >
          <div className={`w-11 h-11 rounded-xl ${color} flex items-center justify-center`}>
            <Icon className="w-5 h-5" />
          </div>
          <div>
            <p className="text-sm text-gray-500">{label}</p>
            <p className="text-2xl font-semibold text-gray-900">{value}</p>
          </div>
        </div>
      ))}
    </div>
  );
}


export default SummaryCards;
