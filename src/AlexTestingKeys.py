import Encrypt.Process as process
from database import Database

file='Test1.txt'
Username= 'Alex'

identifier=input('What? ')
if identifier == '1':
    key=process.Sender(file) #NEED TO VERIFY
    x=Database                   #--------------
    Database.addKey(Username,key)#--------------
    file=file+'E'        #--------------
else:
    file=file+'E'
    key=Database.getKey(Username)
    x=Database
    process.Receiver(file,key)
    print('The file has now been decompressed')

