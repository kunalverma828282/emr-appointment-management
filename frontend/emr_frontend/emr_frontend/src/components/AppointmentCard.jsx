import {
  PencilSquareIcon,
  TrashIcon,
} from "@heroicons/react/24/outline";

import {
  CheckCircleIcon,
  ClockIcon,
  XCircleIcon,
  VideoCameraIcon,
  UserIcon,
  BuildingOfficeIcon,
  PhoneIcon,
  EnvelopeIcon,
} from "@heroicons/react/24/solid";

const STATUS_CONFIG = {
  Confirmed: {
    color: "bg-green-100 text-green-700",
    icon: CheckCircleIcon,
  },
  Scheduled: {
    color: "bg-blue-100 text-blue-700",
    icon: ClockIcon,
  },
  Upcoming: {
    color: "bg-indigo-100 text-indigo-700",
    icon: ClockIcon,
  },
  Cancelled: {
    color: "bg-red-100 text-red-700",
    icon: XCircleIcon,
  },
};

function AppointmentCard({ appt, onStatusChange }) {
  const StatusIcon = STATUS_CONFIG[appt.status]?.icon;

  return (
    <div className="bg-white rounded-xl border shadow-[0_8px_24px_rgba(0,0,0,0.06)] p-5 flex gap-4">
      {/* Avatar */}
      <div className="w-11 h-11 rounded-full bg-blue-100 text-blue-700 flex items-center justify-center font-semibold">
        {appt.name.charAt(0)}
      </div>

      {/* Details */}
      <div className="flex-1">
        <div className="flex justify-between items-start">
          <div>
            <p className="font-semibold text-gray-900">{appt.name}</p>
            <p className="text-sm text-gray-500">
              {appt.date} • {appt.time} • {appt.duration} min
            </p>
          </div>

          <span
            className={`flex items-center gap-1 text-xs px-3 py-1 rounded-full ${STATUS_CONFIG[appt.status]?.color}`}
          >
            {StatusIcon && <StatusIcon className="w-4 h-4" />}
            {appt.status}
          </span>
        </div>

        <p className="text-sm text-gray-600 mt-2">
          <strong>{appt.type}</strong> — {appt.reason}
        </p>

        <p className="text-xs text-gray-400 mt-1">{appt.notes}</p>

        {/* Meta */}
        <div className="flex flex-wrap gap-4 mt-3 text-xs text-gray-500">
          <span className="flex items-center gap-1">
            <UserIcon className="w-4 h-4 text-gray-400" />
            {appt.doctorName}
          </span>

          {appt.mode === "In-Person" && (
            <span className="flex items-center gap-1">
              <BuildingOfficeIcon className="w-4 h-4 text-gray-400" />
              In-Person
            </span>
          )}

          {appt.mode === "Virtual" && (
            <span className="flex items-center gap-1 text-purple-600">
              <VideoCameraIcon className="w-4 h-4" />
              Video Call
            </span>
          )}
        </div>

        <div className="flex gap-4 mt-2 text-xs text-gray-400">
          <span className="flex items-center gap-1">
            <PhoneIcon className="w-4 h-4" />
            {appt.phone}
          </span>
          <span className="flex items-center gap-1">
            <EnvelopeIcon className="w-4 h-4" />
            {appt.email}
          </span>
        </div>
      </div>

      {/* Actions */}
<div className="flex flex-col justify-between items-end">
  {/* Status dropdown */}
  <select
    value={appt.status}
    onChange={(e) => onStatusChange(appt.id, e.target.value)}
    className="border rounded-md px-2 py-1 text-sm"
  >
    <option>Confirmed</option>
    <option>Scheduled</option>
    <option>Upcoming</option>
    <option>Cancelled</option>
  </select>

  {/* Edit / Delete at bottom */}
  <div className="flex gap-3 mt-6 text-gray-400">
    <PencilSquareIcon className="w-5 h-5 hover:text-blue-600 cursor-pointer" />
    <TrashIcon className="w-5 h-5 hover:text-red-600 cursor-pointer" />
  </div>
</div>
    </div>
  );
}
export default AppointmentCard;
