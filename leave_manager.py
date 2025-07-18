import json
import re
from datetime import datetime

class LeaveManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.records = self._load_records()

    def _load_records(self):
        try:
            with open(self.file_path, "r") as f:
                info = json.load(f)
                if not all(k in info for k in ["Leaves_Data_Internal_Employees", "holiday_calendar"]):
                    raise ValueError("Missing expected keys.")
                return info
        except Exception as err:
            print(f"Load error: {err}")
            return {
                "Leaves_Data_Internal_Employees": {
                    "Alice Johnson": {"balance": 10, "history": ["2024-12-12", "2025-01-02"]},
                    "Bob Smith": {"balance": 5, "history": []},
                    "Charlie Davis": {"balance": 8, "history": ["2025-01-02"]}
                },
                "holiday_calendar": [
                    "2025-01-01", "2025-01-20", "2025-02-17", "2025-05-26",
                    "2025-07-04", "2025-09-01", "2025-11-27", "2025-11-28",
                    "2025-12-25", "2025-12-31"
                ]
            }

    def _write_records(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump(self.records, f, indent=2)
            return True
        except Exception as err:
            print(f"Save error: {err}")
            return False

    def get_leave_balance(self, name: str):
        emp_data = self.records.get("Leaves_Data_Internal_Employees", {})
        if name not in emp_data:
            return {"success": False, "message": f"No data found for {name}."}
        info = emp_data[name]
        return {"success": True, "employee_name": name, "leave_balance": info["balance"], "leave_history": info["history"]}

    def request_leave(self, name: str, date: str):
        if not self._validate_date_format(date):
            return {"success": False, "message": "Date must be YYYY-MM-DD format."}

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return {"success": False, "message": "Date is not valid."}

        emp_data = self.records.get("Leaves_Data_Internal_Employees", {})
        holidays = self.records.get("holiday_calendar", [])

        if name not in emp_data:
            return {"success": False, "message": f"Employee {name} not found."}

        if date in holidays:
            return {"success": False, "message": f"{date} is a holiday."}

        if date in emp_data[name]["history"]:
            return {"success": False, "message": f"Leave already requested for {date}."}

        if emp_data[name]["balance"] <= 0:
            return {"success": False, "message": "No leave balance remaining."}

        emp_data[name]["history"].append(date)
        emp_data[name]["balance"] -= 1

        if not self._write_records():
            emp_data[name]["history"].remove(date)
            emp_data[name]["balance"] += 1
            return {"success": False, "message": "Could not save data."}

        return {
            "success": True,
            "message": f"Leave recorded for {date}.",
            "updated_balance": emp_data[name]["balance"],
            "updated_history": emp_data[name]["history"]
        }

    def list_employees(self):
        return {"success": True, "employee_names": sorted(self.records.get("Leaves_Data_Internal_Employees", {}).keys())}

    def list_holidays(self):
        return {"success": True, "holidays": sorted(self.records.get("holiday_calendar", []))}

    def _validate_date_format(self, text: str):
        return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', text))
