import pyautogui
import time
import keyboard
import random
import win32api, win32con
from os import system

x = 0
y = 0
# 1377, 328 -> 454
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while not keyboard.is_pressed('q'):
    for i in range(1,5):
        click(1377, 328)
        time.sleep(.1)
        click(1377, 454)