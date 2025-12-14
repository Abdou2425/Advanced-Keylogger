import os
from PIL import ImageGrab
import time
import os
from dotenv import load_dotenv
load_dotenv()  

file_path = os.getenv("FILE_PATH")
extend = "\\"

def screenshot():
    timestamp = time.strftime("%Y%m%d_%H%M%S")  # Unique timestamp for each screenshot
    screenshot_filename = f"screenshot_{timestamp}.png"
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_filename)
