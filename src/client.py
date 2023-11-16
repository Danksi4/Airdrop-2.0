import tqdm
import os
import socket

SEPERATOR = '<SEPERATOR>'
BUFFER_SIZE = 4096

host = '10.0.0.215'
port = 5001
filename = 'file.txt'
# get the size of the file in bytes
filesize = os.path.getsize(filename)
# create the client socket
s = socket.socket()
# connecting to the server
print(f'[+] Connecting to {host}:{port}')
s.connect((host, port))
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
