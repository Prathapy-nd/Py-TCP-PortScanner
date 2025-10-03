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
        # Attempt connection to the target (IP, Port)
        # connect_ex returns an error indicator (0 means success)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            # If connect_ex returns 0, the port is OPEN
            print(f"Port {port}: OPEN")
        
        s.close() # Always close the socket after the check

    except socket.timeout:
        # We explicitly skip closed ports (where timeout occurs)
        pass 
    except Exception as e:
        # Catch any unexpected errors (less common)
        # print(f"An unexpected error occurred on port {port}: {e}")
        pass
    finally:
        s.close()

# --- Main Logic with Threading ---
def main_scanner():
    """Handles user input and creates threads for the port range."""
    
    # 1. Input Handling (You should replace this with a powerful tool like 'argparse' later!)
    target = input("Enter the target IP or hostname: ") 
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[!] Invalid Hostname/IP. Exiting.")
        sys.exit()

    # Define the range of ports to scan
    start_port = 1
    end_port = 1024
    
    print("-" * 50)
    print(f"Scanning Target: {target_ip}")
    print(f"Port Range: {start_port}-{end_port}")
    print(f"Scan Started at: {str(datetime.now().strftime('%H:%M:%S'))}")
    print("-" * 50)

    # 2. The Multi-threading Loop
    for port in range(start_port, end_port + 1):
        # Create a new thread, targeting the scan_port function
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        
        # Start the thread execution
        thread.start()

if __name__ == "__main__":
    main_scanner()
