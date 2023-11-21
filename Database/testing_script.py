#from database import database

#x = database()
#x.storeUser("Bradley","192.168.55.1")

"""
import webbrowser    
url='https://www.google.com'
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)
"""

import requests
response = requests.get("https://ww.google.com", timeout=1)
print(response)