from cryptography.fernet import Fernet
import sys #Dont need yet, just toying with ideas on what to do
import random

class encryption():
    def __init__(self,name=''):
        self.name=name
        self.ID=str(random.random())
        self.key=Fernet.generate_key()
        with open('tempkeys/key.key'+self.ID,'wb') as key_file:
            key_file.write(self.key)

    def load_key(self):
        load=open('tempkeys/key.key'+self.ID,'rb').read()
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
    

'''Test example on how to call, need to figure out why it creates the same key when called withh diff objects.'''
message=input('First message: ')
message2=input('Second message: ')
keytest=encryption(message)
keytest2=encryption(message2)
keytest2.load_key()
print("The key is:",keytest.load_key())
x=keytest.encrypt()
print('The encrypted message is:',x)
Final=keytest.decrypt(x)
print('The final message is:',Final)





        