import pyautogui
import time
width, height = pyautogui.size() #display size
#print(width)
#print(height)

#print(pyautogui.position()) #prints out current mouse position
print(pyautogui.position())
original_x, original_y = pyautogui.position()
pyautogui.hotkey('win')

