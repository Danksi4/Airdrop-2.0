import customtkinter

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark-blue")

class App(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Airdrop 2.0")
        self.geometry("800x600")
        
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Username")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.entryBox)
        
  
    def start(self):
        self.mainloop()

    def entryBox(self):
        print(self.entry.get())
        self.entry.delete(0,len(self.entry.get()))
        # FIXME: add adduser method to verify username is not already taken

if __name__=="__main__":
    program = App()
    program.start()




