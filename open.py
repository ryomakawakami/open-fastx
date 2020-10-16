import pyautogui
from PIL import ImageGrab
import time

wifi = (1153, 746)
pulse = (1075, 184)
pulse2 = (407, 254)
connect = (478, 320)
proceed = (404, 660)
next = (638, 708)
next2 = (644, 417)
password = (404, 394)

def click(pos, colorPos = None, color = None, sleep = 0.01):
    pyautogui.click(pos[0], pos[1])
    if colorPos:
        while ImageGrab.grab().getpixel(colorPos) != color:
            pass
    time.sleep(sleep)

# Connect to Pulse
click(wifi, (1058, 173), (255, 255, 255))
click(pulse, (352, 272), (0, 118, 215))
click(pulse2, (512, 318), (194, 194, 194))
click(connect, (413, 659), (48, 48, 48))
click(proceed)
click(next)
click(next2)
click(password)
click(password)
pyautogui.write('push')
pyautogui.press('enter')
