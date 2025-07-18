import json
import os
from mcp.server.fastmcp import FastMCP
from leave_manager_alt import LeaveManager

base_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(base_dir, "Mock_Data.json")

print("Checking available files:", os.listdir(base_dir))
print(f"Leave data file path: {data_file}")

manager = LeaveManager(data_file)

mcp_app = FastMCP("alt-sjsu-leave-system")

@mcp_app.tool()
def get_leave_balance(employee_name: str):
    return manager.get_leave_balance(employee_name)

@mcp_app.tool()
def request_leave(employee_name: str, leave_date: str):
    return manager.request_leave(employee_name, leave_date)

@mcp_app.tool()
def list_employees():
    return manager.list_employees()

@mcp_app.tool()
def list_holidays():
    return manager.list_holidays()

if __name__ == "__main__":
    print("Launching Alternate Leave Management Server...")
    try:
        mcp_app.run(transport="stdio")
    except Exception as ex:
        print(f"Startup failed: {ex}")
