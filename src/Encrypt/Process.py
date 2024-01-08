from Encrypt.DandCclasses import DandC
from Encrypt.testencrypt import fileEncryption

def Sender(file):
    encryption=fileEncryption()
    key=encryption.load_key()
    #This is where it would push key to sheets
    encryption.encrypt(file)
    x=DandC(file+'E')
    x.compressor()
    return key
    
def Receiver(file,key='0'):
    y=DandC(file)
    y.decompressor()
    decryption=fileEncryption()
    decryption.decrypt(file,'S',key) #<--- for when sheets implemented add 'S',key args
    return -1

if __name__=='__main__':
    files='Test.txt'
    Sender(files)
    Receiver(files+'E')#add two more arguments when sheets implemented
    #add 's', as well as the key pulled from sheets.
