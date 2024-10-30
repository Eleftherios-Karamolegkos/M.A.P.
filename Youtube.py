import time
import keyboard
import pyautogui
def search_google():
    if pyautogui.locateOnScreen(r"C:\Users\lefte\Pictures\Screenshots\Screenshot 2024-10-09 162517.png", confidence=0.4) !=None:
        print("Yes")
        time.sleep(2)
        camp_google = pyautogui.locateOnScreen(r"C:\Users\lefte\Pictures\Screenshots\Screenshot 2024-10-09 162517.png", confidence=0.4)
        pyautogui.click(camp_google)
        time.sleep(5)
        pyautogui.write("https://www.youtube.com")
        pyautogui.press('enter')
        time.sleep(5)
search_google()