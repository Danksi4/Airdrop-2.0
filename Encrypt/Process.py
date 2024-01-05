from DandCclasses import DandC
from testencrypt import fileEncryption


def Sender(file):
    encryption=fileEncryption()
    key=encryption.load_key()
    #This is where it would push key to sheets
    encryption.encrypt(file)
    x=DandC(file)
    x.compressor()
    return -1
    
def Receiver(file):
    y=DandC(file)
    y.decompressor()
    decryption=fileEncryption()
    #This is where it would pull the key from sheets
    decryption.decrypt(file,'S',id) #<--- for when sheets implemented
    return -1

if __name__=='__main__':
    files='Test.txt'
    Sender(files)
    Receiver(files)
