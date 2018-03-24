#Import for our manipulation of the curson/keyboard
import pyautogui

def click_power_on():
    pyautogui.click(340, 450)

def click_power_off():
    pyautogui.click(380,450)

def input_video():
    pyautogui.click(465,435)

def input_s_video():
    pyautogui.click(685,435)

def input_comp_1():
    pyautogui.click(465,485)

def input_comp_2():
    pyautogui.click(685,485)


click_power_on()