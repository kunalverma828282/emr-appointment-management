import { DayPicker } from "react-day-picker";
import "react-day-picker/dist/style.css";

function CalendarWidget({ selectedDate, onDateChange }) {
  return (
    <div className="bg-white rounded-xl border shadow-sm p-4">
      <DayPicker
        mode="single"
        selected={selectedDate ? new Date(selectedDate + "T00:00:00") : undefined}
        onSelect={(date) => {
          if (!date) return;
          onDateChange(date.toLocaleDateString("en-CA"));
        }}
      />
    </div>
  );
}

export default CalendarWidget;
