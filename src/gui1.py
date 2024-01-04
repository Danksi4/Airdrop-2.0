import customtkinter

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark-blue")

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Airdrop 2.0")
        self.geometry("800x600")

    
        
    def start(self):
        self.mainloop()

if __name__=="__main__":
    program = App()
    program.start()




