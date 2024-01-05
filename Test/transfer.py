import socket
import tqdm
import os

BUFFER_SIZE = 4096
SEPERATOR = '<SEPERATOR>'
SERVER_HOST = '0.0.0.0' # indicates all local machine IP addresses for use
SERVER_PORT = 5001 # match with the client port

def send(hostIPAddress=str,filename=str):
    ## The send function employs the client code in order to send files to the server
    
    ## Connection
    filesize = os.path.getsize(filename)  # get the size of the file in bytes
    s = socket.socket()  # create the client socket
    print(f'[+] Connecting to {hostIPAddress}:{SERVER_PORT}')  # connecting to the server
    s.connect((hostIPAddress, SERVER_PORT))
    print('Connected')
    # send the file name and file size information to the server
    s.send(f'{filename}{SEPERATOR}{filesize}'.encode()) # calls encode() to convert the information to bytes

    ## SEND THE FILE AND DISPLAY THE PROGRESS
    progress = tqdm.tqdm(range(filesize), f'Sending {filename}', unit = 'B', unit_scale = True, unit_divisor = 1024) # creates the progress bar for file transmission
    with open(filename, 'rb') as f: # opens the file to read binary 
        while True:
            # read the bytes from the file in 4096 byte increments as specified by BUFFER_SIZE
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break # file is done sending
            s.sendall(bytes_read) # sendall to assure file is transmitted
            # update the progress bar based on the amount of bytes read
            progress.update(len(bytes_read))
    #close the socket
    s.close()


def receive():
    ## The receive function employs the server code in order to recieve files from the client
    
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
    filesize = int(filesize) # converts filesize from str to int
    print(f"filesize: {filesize}")
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