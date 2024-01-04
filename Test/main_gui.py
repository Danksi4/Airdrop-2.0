from database import Database
import customtkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Airdrop 2.0")
        self.geometry("800x600")
  
    def start(self):
        self.mainloop()

if __name__=="__main__":
    #x = Database()
    program = App()
    program.start()