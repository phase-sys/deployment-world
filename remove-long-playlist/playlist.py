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
    
def getnclick():
    refx = pyautogui.locateOnScreen('ref.png', grayscale = True, confidence = 0.80).left
    refy = pyautogui.locateOnScreen('ref.png', grayscale = True, confidence = 0.80).top
    click(refx, refy)
    time.sleep(.75)
    refx1 = pyautogui.locateOnScreen('ref1.png', grayscale = True, confidence = 0.80).left
    refy1 = pyautogui.locateOnScreen('ref1.png', grayscale = True, confidence = 0.80).top
    click(refx1+25, refy1+25)

while not keyboard.is_pressed('q'):
    try:
        getnclick()
    except:
        print("Repeat")