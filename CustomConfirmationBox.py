import pyautogui
import time

time.sleep(4)

answer = pyautogui.confirm(text="Do you want to close this window ?", title="Learn With Kens", buttons=["OK", "Cancel"])

if answer == "OK":
    pyautogui.keyDown("alt")
    pyautogui.press("f4")
    pyautogui.keyUp("alt")