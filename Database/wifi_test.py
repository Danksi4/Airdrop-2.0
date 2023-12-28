import socket

def is_connected():
    try:
        # connect to the host -- google.com
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

if is_connected():
    print("You are connected to the internet.")
else:
    print("You are not connected to the internet.")