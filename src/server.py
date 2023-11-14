import socket
import tqdm
import os

SERVER_HOST = '0.0.0.0' # indicates all local machine IP addresses for use
SERVER_PORT = 5001 # match with the client port
BUFFER_SIZE = 4096 # max bytes that can be received each time
SEPERATOR = '<SEPERATOR'

s = socket.socket() # creates the TCP socket from the socket module
s.bind((SERVER_HOST, SERVER_PORT)) # bind this socket to the server socket
s.listen(5) # will allow 5 unaccepted connections before refusing to connect
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
client_socket, address = s.accept() # accepts client connection if it exists
print(f"[+] {address} is connected.")
received = client_socket.recv(BUFFER_SIZE).decode() # receive using the client socket
filename, filesize = received.split(SEPERATOR)
filename = os.path.basename(filename) # removes the absolute path of the file
filesize = int(filesize) # concerts filezise from str to int

