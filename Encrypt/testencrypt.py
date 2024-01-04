from cryptography.fernet import Fernet
import sys #Dont need yet, just toying with ideas on what to do
import random

class encryption():
    def __init__(self,name=''):
        self.name=name
        self.ID=str(random.random())
        self.key=Fernet.generate_key()
        with open('tempkeys/key#'+self.ID,'wb') as key_file:
            key_file.write(self.key)

    def load_key(self):
        load=open('tempkeys/key#'+self.ID,'rb').read()
        return load
    
    def encrypt(self):
        message=self.name.encode()
        f=Fernet(self.key)
        encrypted=f.encrypt(message)
        return encrypted
    
    def decrypt(self,encrypted):
        f=Fernet(self.key)
        decrypted=f.decrypt(encrypted)
        final=decrypted.decode()
        return final

class fileEncryption(encryption):
    def encrypt(self, filename):
        f = Fernet(self.key)
        with open(filename, 'rb') as file_obj:
            file_content = file_obj.read()
        encrypted = f.encrypt(file_content)
        with open(filename, 'wb') as file_obj:
            file_obj.write(encrypted)
        return -1

    def decrypt(self, filename):
        f = Fernet(self.key)
        with open(filename, 'rb') as file_obj:
            encrypted_content = file_obj.read()
        decrypted = f.decrypt(encrypted_content)
        with open(filename, 'wb') as file_obj:
            file_obj.write(decrypted)
        return -1
    
'''Test example on how to call'''
print('-'*20)
print('Text Transfer Test')
print('-'*20)
message=input('Message to be encrypted: ')
keytest=encryption(message)
print("The key is:",keytest.load_key())
x=keytest.encrypt()
print('The encrypted message is:',x)
Final=keytest.decrypt(x)
print('The final message is:',Final)


'''Test for file encryption'''
print('-'*20)
print('File Transfer Test')
print('-'*20)
file='Test.txt'
filetest=fileEncryption()
print("The key is:",filetest.load_key())
filetest.encrypt(file)
with open(file, 'rb') as fileobj:
    container=fileobj.read()
print('The encrypted file contains: '+str(container))
filetest.decrypt(file)
with open(file) as newobj:
    newcontainer=newobj.readlines()
print('The decrypted file contains:')
print(newcontainer)



        
