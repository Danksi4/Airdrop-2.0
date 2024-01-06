import customtkinter
import database
import transfer
#import Encrypt.Process as process

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")

# class ToplevelWindow(customtkinter.CTkToplevel):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         #self.wm_attributes('-topmost', True)
#         w = 800 # width for the Tk root
#         h = 650 # height for the Tk root
#         ws = self.winfo_screenwidth() # width of the screen
#         hs = self.winfo_screenheight() # height of the screen        
#         x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk root window
#         y = (hs/2) - (h/2)
#         self.geometry('%dx%d+%d+%d' % (w, h, x, y)) # screen dimensions and spawn location
        
#         self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
#         self.label.pack(padx=20, pady=20)
        
class App(customtkinter.CTk):
    
    USER = None
    IPADDRESS = None
    
    def __init__(self, database, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = database

        ## Checking if the computer knows who it is
        
        try:
            with open('accountInfo.txt','r') as file:
                self.USER, self.IPADDRESS = file.read().split()
                print(self.USER)
                print(self.IPADDRESS)
        except FileNotFoundError:
            print(f"File '{'accountInfo.txt'}' not found.")
        except ValueError:
            pass
        
        ## Setting up the main gui interface 

        self.title("Airdrop 2.0")
        w = 800 # width for the Tk root
        h = 650 # height for the Tk root
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen        
        x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk root window
        y = (hs/2) - (h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y)) # screen dimensions and spawn location

        ## Deciding if the user needs to add their username and ip address or not
         
        self.main()
        if (self.USER == None) and (self.IPADDRESS == None):
            self.addUserForFirstTime()
        else:
            self.main()


    def main(self):
        # create a textbox for entering the recipients username
        self.receiver = customtkinter.CTkEntry(self, placeholder_text="Enter Recipient Username")
        self.receiver.grid(row=0, column=2, sticky="we", padx=(12, 0), pady=12)
        # create a textbox for entering the filename
        self.filename = customtkinter.CTkEntry(self, placeholder_text="Enter Filename You Wish to Send")
        self.filename.grid(row=1, column=2, sticky="we", padx=(12, 0), pady=12)
        # create a send button that calls the sendFile() function when pressed
        self.sendbutton = customtkinter.CTkButton(self, text="Send File", command=self.sendFile)
        self.sendbutton.grid(row=2, column=2, sticky="w", padx=(12, 0), pady=12)


    def addUserForFirstTime(self,errorMessage=""):
        # FIXME automatically ping their ip address to validate that it works
        self.clearScreen()

        self.label = customtkinter.CTkLabel(self, text="Welcome to Airdrop 2.0! It looks like you"
                                            " aren't entered into our database yet. Please enter your"
                                            " username and ip address", fg_color="transparent")
        self.label.grid(row=1, column=0, columnspan = 3, sticky="w", padx=(12, 0), pady=12)

        self.errorLabel = customtkinter.CTkLabel(self, text=f"{errorMessage}", fg_color="transparent")
        self.errorLabel.grid(row=0, column=0, columnspan = 3, sticky="w", padx=(12, 0), pady=12)

        self.username = customtkinter.CTkEntry(self, placeholder_text="Enter Username")
        self.username.grid(row=2, column=0, sticky="we", padx=(12, 0), pady=12)

        self.ipaddress = customtkinter.CTkEntry(self, placeholder_text="Enter IP Address")
        self.ipaddress.grid(row=2, column=1, sticky="we", padx=(12, 0), pady=12)

        self.submitbutton = customtkinter.CTkButton(self, text="Submit", command=self.entryBox)
        self.submitbutton.grid(row=2, column=2, sticky="w", padx=(12, 0), pady=12)
    

    def clearScreen(self):
        for widget in self.winfo_children():
            widget.destroy()


    def button_click_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Test")
        print("Number:", dialog.get_input())


    def entryBox(self,event=None):
        if self.db.findUser(self.username.get()) == True: # if their username is already in use
            self.addUserForFirstTime(
                f"{self.username.get()} already exists. Please enter a different username")
        else:
            self.db.addUser(self.username.get(),self.ipaddress.get())
            self.username.delete(0,len(self.username.get()))
            self.ipaddress.delete(0,len(self.ipaddress.get()))
            self.clearScreen()
            self.main()


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
    

    def start(self):
        self.mainloop()


if __name__=="__main__":
    db = database.Database()
    program = App(db)
    program.start()