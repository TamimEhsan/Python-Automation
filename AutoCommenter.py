import pyautogui

pyautogui.PAUSE = 0.5
height,width = pyautogui.position()
pyautogui.click(height,width)
for i in range(10):
    string = "auto "+str(i)
    pyautogui.typewrite(string)
    pyautogui.press('enter')
