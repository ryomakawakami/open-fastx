import pyautogui
import time

wifi = (1153, 746)
pulse = (1075, 184)
pulse2 = (407, 254)
connect = (478, 320)
proceed = (404, 660)
next = (638, 708)
next2 = (644, 417)
password = (411, 397)

def click(pos, x = 0.1):
    pyautogui.click(pos[0], pos[1])
    time.sleep(x)

# Connect to Pulse
click(wifi, 1)
click(pulse, 1)
click(pulse2)
click(connect, 1)
click(proceed)
click(next)
click(next2, 0.15)
click(password)
pyautogui.write('push')
pyautogui.press('enter')
