import pyautogui
import time
import keyboard
import random
import win32api, win32con
from os import system

x = 0
y = 0

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def getnclick(n):
    x = pyautogui.locateOnScreen('skip'+ n +'.png', grayscale = True, confidence = 0.80).left
    y = pyautogui.locateOnScreen('skip'+ n +'.png', grayscale = True, confidence = 0.80).top
    click(x+50, y+25)
    time.sleep(1)

while not keyboard.is_pressed('q'):
    try:
        for i in range(1,5):
            if pyautogui.locateOnScreen('skip'+ str(i) +'.png', grayscale = True, confidence = 0.80) != None:
                getnclick(str(i))
    except:
        print("Repeat")