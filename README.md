# SJSU MCP Leave Manager 🌟

Welcome to **SJSU MCP LeaveManager**! 🚀 This is an automated employee leave management system built for San Jose State University (SJSU) using the Model Context Protocol (MCP) server. It streamlines leave applications, balance checks, and enforces constraints like holiday schedules and leave balance limits. The system uses `Mock_Data.json` as an in-memory database for employee leave records and holiday calendars. 📅

## ✨ Features

- **Check Leave Balance** ✅: Employees can query their remaining leave days and view their leave history.
- **Apply for Leave** 📝: Request leave for specific dates with validations to:
  - Prevent duplicate leave requests for the same date.
  - Ensure sufficient leave balance.
  - Block leave requests on official holidays.
- **List Employees** 👥: Retrieve a sorted list of all employees in the system.
- **List Holidays** 🎉: View the official holiday calendar.

## 🛠️ Tech Stack

- **Python** 🐍: Core language for the MCP server and leave management logic.
- **FastMCP** ⚡: Framework for building the MCP server.
- **JSON** 📄: In-memory database using `Mock_Data.json`.
- **Claude Desktop** 💻: For testing natural language queries.

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+ 🐍
- `fastmcp` library (`pip install fastmcp`) 📦
- `Mock_Data.json` file in the project directory 📂
- Claude Desktop for testing natural language queries 🖥️

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sjsu-mcp-leavemanager.git
   cd sjsu-mcp-leavemanager

2. Install dependencies:
   ```bash
   pip install fastmcp
   ```
3. Ensure Mock_Data.json is in the project directory with this structure.
4. Run the MCP server:
   ```bash
   python mcp_server.py
   ```


 ## 📚 Usage
Start the MCP server:
```bash

python mcp_server.py
```
### Connect to the server using Claude Desktop to send natural language queries. 🖱️
Example queries:
"How many leaves are available for employee Alice Johnson?" ❓  
"Request a leave for Bob Smith on 2025-03-15." 📅  
"List all employees." 👥  
"Show the holiday calendar." 🎉   
"Can Charlie Davis take a leave on 2025-07-04?" 🚫  

## Sample Output
### Query: "How many leaves are available for employee Alice Johnson?"
<img src="https://raw.githubusercontent.com/Sanjana130820/Mcp-leave-manager/main/images/alice_balance.png" alt="Alice Balance">

## Future Enhancements for SJSU MCP LeaveManager
Here are concise future enhancements to improve SJSU MCP LeaveManager:

### Multi-Day Leaves 📅
Support date range requests (e.g., 2025-03-10 to 2025-03-12). Update request_leave to handle ranges.
Benefit: Simplifies consecutive leave requests.
### Leave Types 🏖️
Add vacation, sick, and personal leave with separate balances. Update Mock_Data.json and methods.
Benefit: Supports diverse leave policies.
### Approval Workflow ✅
Add "pending" status for leave requests and a manager approval tool.
Benefit: Aligns with HR processes.
### Notifications 📧
Send email/in-app alerts for request status and balance updates. Use smtplib or APIs.
Benefit: Improves communication.
### Persistent Database 💾
Switch to SQLite/MongoDB for scalability. Update LeaveManager for database queries.
Benefit: Ensures data persistence.

## 📌 License

This project is for educational and internal simulation purposes only.
 

