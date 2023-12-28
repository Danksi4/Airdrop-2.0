import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ------------------ Setting up Google Sheets API -----------------------           
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("secret_key.json", scopes=scope)
client = gspread.authorize(creds)
# FIXME the below line doesn't work
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
            # print(cell)
            # row = cell.row
            # column = cell.column + 1
            # print(row, column)
        else:
            print(f"Hmmmm. The username {name} is not in our system.") 
            return False 
    
    def sheetDump(self):
        print(worksheet.get_all_values())

print("hello")
# x = database()
# x.findUser("Maddy")
# #x.getUser("Maddy")