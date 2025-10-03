# Py-TCP-PortScanner
A custom, multithreaded TCP Port Scanner written in Python, demonstrating networking fundamentals, exception handling, and performance optimization for ethical hacking.

Key Features :

✅ Speed
•	Multithreaded Execution: Utilizes Python's threading module to check multiple ports simultaneously, drastically reducing scan time on large port ranges.

✅ Reliability
•	Robust Exception Handling: Implements detailed try...except blocks to gracefully manage network issues (like ConnectionRefused or socket.timeout), guaranteeing the script never crashes and always delivers a clear status for each port.

✅ Efficiency
•	Custom Timeout Control: Utilizes Python's socket.settimeout() to enforce a brief 0.5-second connection limit, preventing the script from hanging on non-responsive ports and ensuring a rapid scan completion.

Technical Deep Dive:

The primary engineering challenge of network scanning is latency (waiting). Since connection attempts are I/O-bound operations that spend significant time waiting for a response or a timeout, the threading module` was implemented. This decision allows the script to check multiple ports simultaneously rather than sequentially, which drastically reduces the total scan time and makes the tool practical for real-world auditing.

🚀 How to Run
1.	Clone the Repository: git clone https://github.com/YourUsername/Py-TCP-PortScanner.git
cd Py-TCP-PortScanner


2.	Install Dependencies: (Even though we use built-in modules, this step shows best practices.)
pip install -r requirements.txt


3.	Execute the Scanner:
python3 threaded_scanner.py
The script will then prompt you for the target IP/Hostname.

