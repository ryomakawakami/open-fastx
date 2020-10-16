import pyautogui
from PIL import ImageGrab
import time

while True:
    x, y = pyautogui.position()
    print(x, y, ImageGrab.grab().getpixel((x, y)))
    time.sleep(1)
#    if pyautogui.confirm(text=str(x) + ' ' + str(y), title='Position', buttons=['OK', 'Cancel']) == 'Cancel':
#        break
