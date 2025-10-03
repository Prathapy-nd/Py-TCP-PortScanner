import socket
import sys
import threading
from datetime import datetime

# --- Configuration ---
# Set a default timeout (seconds) for all socket operations
socket.setdefaulttimeout(0.5) 

# --- Core Scan Logic ---
def scan_port(target_ip, port):
    """
    Attempts to connect to a single port on the target IP using the socket module.
    This function will be run by multiple threads simultaneously.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # connect_ex returns an error indicator (0 means success)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            # If connect_ex returns 0, the port is OPEN
            print(f"Port {port}: OPEN")
        
    except Exception:
        # We catch exceptions quietly and skip (most closed ports result in timeouts)
        pass
    finally:
        s.close() # Ensure the socket is always closed

# --- Main Logic with Threading and .join() FIX ---
def main_scanner():
    """Handles user input, creates threads, and waits for them to complete."""
    
    target = input("Enter the target IP or hostname: ") 
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[!] Invalid Hostname/IP. Exiting.")
        sys.exit()

    start_port = 1
    end_port = 1024
    
    print("-" * 50)
    print(f"Scanning Target: {target_ip}")
    print(f"Port Range: {start_port}-{end_port}")
    print(f"Scan Started at: {str(datetime.now().strftime('%H:%M:%S'))}")
    print("-" * 50)

    # 1. List to hold all thread objects
    all_threads = []

    # 2. The Multi-threading Loop (creates and starts threads)
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        thread.start()
        all_threads.append(thread) 

    # 3. The Joining Loop (waits for all threads to finish)
    for thread in all_threads:
        thread.join()
        
    print("-" * 50)
    print(f"Scan complete for {target_ip}. Total ports checked: {end_port}.")
    print("-" * 50)

if __name__ == "__main__":
    main_scanner()
