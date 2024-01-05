import customtkinter
import database
import transfer

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):

    def __init__(self, database, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Airdrop 2.0")
        self.geometry("800x600")
        self.db = database
    
        self.username = customtkinter.CTkEntry(self, placeholder_text="Enter Username")
        self.username.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)

        self.ipaddress = customtkinter.CTkEntry(self, placeholder_text="Enter IP Address")
        self.ipaddress.grid(row=1, column=0, sticky="we", padx=(12, 0), pady=12)

        self.button = customtkinter.CTkButton(self, text="Submit", command=self.entryBox)
        self.button.grid(row=2, column=0, sticky="w", padx=(12, 0), pady=12)
        #self.entry.bind("<Return>", self.entryBox) # call entryBox method when return key is pressed
        
    def start(self):
        self.mainloop()

    def entryBox(self,event=None):
        self.db.addUser(self.username.get(),self.ipaddress.get())
        self.username.delete(0,len(self.username.get()))
        self.ipaddress.delete(0,len(self.ipaddress.get()))

    def fileLocation():
        pass

    def findClient():
        pass

    def sendFile():
        transfer.send()

    def receiveFile():
        transfer.receive()


if __name__=="__main__":
    db = database.Database()
    program = App(db)
    program.start()