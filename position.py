import pyautogui

while True:
    x, y = pyautogui.position()
    if pyautogui.confirm(text=str(x) + ' ' + str(y), title='Position', buttons=['OK', 'Cancel']) == 'Cancel':
        break
