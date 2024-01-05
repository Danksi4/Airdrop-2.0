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

# ------------------ The Database Class -----------------------           
class Database():
    def __init__(self):
        pass

    def findUser(self,name=str): # determines if the user exists in the database
            if worksheet.find(str(name)) is not None:
                print(f"The username {name} is indeed in the database.") 
                return True
            else:
                print(f"The username {name} is not found in the database.") 
                return False
            
    def addUser(self,name=str,address=str): # adds the user and ip address
        if self.findUser(name) == False: # if the username is not already in use
            worksheet.append_row([name,address])
            print(f"The username {name} has been added to the database.") 
        else:
            print(f"Please choose a different user name. {name} is already taken.") 
            return False
        
    def getUserAddress(self,name=str): # returns the user's ip address
        if self.findUser(name) == True: # if the username exists
            cell = worksheet.find(name)
            print(worksheet.cell(cell.row, (cell.col+1)).value)
        else:
            print(f"Hmmmm. The username {name} is not in our system.") 
            return False 
    
    def sheetDump(self): # dumps all sheet values
        print(worksheet.get_all_values())

    def addKey(self,name=str,key=str):
        if self.findUser(name) == False: # if the username is not already in use
            worksheet.append_row([name,address])
            print(f"The username {name} has been added to the database.") 
        else:
            print(f"Please choose a different user name. {name} is already taken.") 
            return False

    def getKey(self,name=str):
        if self.findUser(name) == True: # if the username exists
            cell = worksheet.find(name)
            key = worksheet.cell(cell.row, (cell.col+2)).value
            if key != None:
                print(key)
                return key
            else:
                print(f"There is no encryption key associated with {name}")
                return False
        else:
            print(f"Hmmmm. The username {name} is not in our system.") 
            return False 
        
if __name__=="__main__":
    x = Database()
    x.addUser("Dan", "dfgfdgfdg")
    x.getKey("Dan")
    