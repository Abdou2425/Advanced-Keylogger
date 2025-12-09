import os
from PIL import ImageGrab
import time

file_path = "C:\\Users\\PC-Service\\OneDrive\\Desktop\\project\\files\\"
extend = "\\"

def screenshot():
    timestamp = time.strftime("%Y%m%d_%H%M%S")  # Unique timestamp for each screenshot
    screenshot_filename = f"screenshot_{timestamp}.png"
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_filename)
