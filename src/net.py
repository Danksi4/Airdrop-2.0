import socket

def get_local_ip():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connect to an external server (Google's public DNS)
        s.connect(("8.8.8.8", 80))

        # Get the local IP address
        local_ip = s.getsockname()[0]

        return local_ip
    except socket.error as e:
        print(f"Error: {e}")
        return None
    finally:
        # Close the socket
        s.close()

# Get and print the local IP address
local_ip_address = get_local_ip()
print(f"Local IP Address: {local_ip_address}")
