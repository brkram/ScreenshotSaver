from PIL import ImageGrab
import time
import os
import webbrowser

PATH = "C:/"
FOLDERNAME = "TempScreenShots/"

full_path = PATH + FOLDERNAME
named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%d_%m_%Y_%H_%M_%S", named_tuple)

final = full_path + time_string + ".png"

if not os.path.exists(full_path):
    os.makedirs(full_path)
im = ImageGrab.grabclipboard()

try:
    im.save(final, 'PNG')
    webbrowser.open(os.path.realpath(full_path))
    print("Hooray")
except:
    pass