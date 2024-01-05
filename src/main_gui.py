import customtkinter
import database
import transfer
#import Encrypt.Process as process

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    
    USER = None
    IPADDRESS = None
    
    def __init__(self, database, *args, **kwargs):
        
        try:
            with open('accountInfo.txt','r') as file:
                self.USER, self.IPADDRESS = file.read().split()
                print(self.USER)
                print(self.IPADDRESS)
        except FileNotFoundError:
            print(f"File '{'accountInfo.txt'}' not found.")

        if (self.USER == None) and (self.IPADDRESS == None):
            pass

        super().__init__(*args, **kwargs)
        self.title("Airdrop 2.0")
        self.geometry("800x600")
        self.db = database
    
        self.username = customtkinter.CTkEntry(self, placeholder_text="Enter Username")
        self.username.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)

        self.ipaddress = customtkinter.CTkEntry(self, placeholder_text="Enter IP Address")
        self.ipaddress.grid(row=1, column=0, sticky="we", padx=(12, 0), pady=12)

        self.submitbutton = customtkinter.CTkButton(self, text="Submit", command=self.entryBox)
        self.submitbutton.grid(row=2, column=0, sticky="w", padx=(12, 0), pady=12)
        # create a textbox for entering the recipients username
        self.receiver = customtkinter.CTkEntry(self, placeholder_text="Enter Recipient Username")
        self.receiver.grid(row=0, column=2, sticky="we", padx=(12, 0), pady=12)
        # create a textbox for entering the filename
        self.filename = customtkinter.CTkEntry(self, placeholder_text="Enter Filename You Wish to Send")
        self.filename.grid(row=1, column=2, sticky="we", padx=(12, 0), pady=12)
        # create a send button that calls the sendFile() function when pressed
        self.sendbutton = customtkinter.CTkButton(self, text="Send File", command=self.sendFile)
        self.sendbutton.grid(row=2, column=2, sticky="w", padx=(12, 0), pady=12)
        
        
    def start(self):
        self.mainloop()

    def entryBox(self,event=None):
        self.db.addUser(self.username.get(),self.ipaddress.get())
        self.username.delete(0,len(self.username.get()))
        self.ipaddress.delete(0,len(self.ipaddress.get()))

    def fileLocation(self):
        pass

    def findClient(self):
        pass

    def sendFile(self):  
        # FIXME once the ip adress is obtained using the username, pass that into the transfer.send() function as the recipients ip
        # get the recipients ip adress using their username
        host_ip = self.db.getUser(self.receiver.get())
        file_name = self.filename.get()
        self.receiver.delete(0,len(self.receiver.get()))
        self.filename.delete(0,len(self.filename.get()))

        transfer.send(host_ip, file_name)


    def receiveFile(self):
        transfer.receive()

if __name__=="__main__":
    db = database.Database()
    program = App(db)
    program.start()