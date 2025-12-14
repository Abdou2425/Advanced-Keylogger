import pygetwindow as gw
import time
import os
from dotenv import load_dotenv
load_dotenv()  

file_path = os.getenv("FILE_PATH")
extend = "\\"

stop_window_tracking = False

def track_active_window(duration=10):
    global stop_window_tracking
    start_time = time.time()
    last_window = None
    with open(file_path + extend + "window_log.txt", "a", encoding="utf-8") as f:  # Use UTF-8 encoding
        while time.time() - start_time < duration:
            active_window = gw.getActiveWindow()
            if active_window and active_window.title != last_window:
                last_window = active_window.title
                try:
                    f.write(f"[WINDOW] Active Window Changed: {last_window}\n")
                    f.flush()
                except UnicodeEncodeError:
                    f.write("[WINDOW] Active Window Changed: [UNREADABLE CHARACTERS]\n")
                    f.flush()
            time.sleep(1)
    stop_window_tracking = True  # Ensuring the flag is set to stop tracking

