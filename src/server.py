import socket
import tqdm
import os

SERVER_HOST = '0.0.0.0' # indicates all local machine IP addresses for use
SERVER_PORT = 5001 # match with the client port
BUFFER_SIZE = 4096 # max bytes that can be received each time
SEPERATOR = '<SEPERATOR'

## CONNECTION
s = socket.socket() # creates the TCP socket from the socket module
s.bind((SERVER_HOST, SERVER_PORT)) # bind this socket to the server socket
s.listen(5) # will allow 5 unaccepted connections before refusing to connect
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
client_socket, address = s.accept() # accepts client connection if it exists
print(f"[+] {address} is connected.")
received = client_socket.recv(BUFFER_SIZE).decode() # receive using the client socket
filename, filesize = received.split(SEPERATOR)
filename = os.path.basename(filename) # removes the absolute path of the file as the client's path
# will be different than the server's path
filesize = int(filesize) # concerts filesize from str to int

## RECEIVING
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, 'wb') as f: # opens the file in binary format for writing
    while True: # a loop of file reading
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read: # if nothing has been received
            break
        f.write(bytes_read)
        progress.update(len(bytes_read)) # updates the progress bar with bytes_read / range(filesize)

client_socket.close()
s.close()
