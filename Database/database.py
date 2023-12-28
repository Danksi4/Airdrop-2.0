import gspread
from oauth2client.service_account import ServiceAccountCredentials
import socket

# ------------------ Connection Test Function -----------------------  
def connectionTest():
    try:
        # connect to the host -- google.com
        socket.create_connection(("www.google.com", 80))
        return True # if connected
    except OSError:
        pass
    return False # if not connected

# ------------------ Setting up Google Sheets API -----------------------           
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("secret_key.json", scopes=scope)
client = gspread.authorize(creds)
assert connectionTest(), "Not connected to the internet"
print("Succesful internet connection")
spreadsheet = client.open("AirdropDatabase")
worksheet = spreadsheet.sheet1

# ------------------ The Database class -----------------------           
class database():
    def __init__(self):
        pass

    def findUser(self,name):
            if worksheet.find(str(name)) is not None:
                return True
            else:
                return False
            
    def addUser(self,name,address):
        if self.getUser(name) == False: # if the username is not already in use
            worksheet.append_row([name,address])
        else:
            print(f"Please choose a different user name. {name} is already taken.") 
            return False
        
    def getUser(self,name):
        if self.findUser(name) == True: # if the username exists
            cell = worksheet.find("Maddy")
            print(worksheet.cell(cell.row, (cell.col+1)).value)
        else:
            print(f"Hmmmm. The username {name} is not in our system.") 
            return False 
    
    def sheetDump(self):
        print(worksheet.get_all_values())

x = database()
x.findUser("Maddy")
x.getUser("Maddy")