import {
  HomeIcon,
  CalendarDaysIcon,
  ClipboardDocumentListIcon,
  Cog6ToothIcon,
} from "@heroicons/react/24/outline";

export default function Sidebar() {
  const icons = [
    HomeIcon,
    CalendarDaysIcon,
    ClipboardDocumentListIcon,
    Cog6ToothIcon,
  ];

  return (
    <aside className="w-16 bg-white border-r min-h-screen flex flex-col items-center py-4 gap-6">
      <div className="w-10 h-10 rounded-xl bg-gray-900 text-white flex items-center justify-center font-semibold">
        M
      </div>

      {icons.map((Icon, i) => (
        <Icon
          key={i}
          className="w-6 h-6 text-gray-400 hover:text-blue-600 cursor-pointer"
        />
      ))}
    </aside>
  );
}
