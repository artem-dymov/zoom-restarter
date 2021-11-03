import pyautogui
import time
import webbrowser

zoom_link = input("Input zoom link: ")

while True:
    zoom_location_active = pyautogui.locateOnScreen('zoom.png')
    zoom_location_inactive = pyautogui.locateOnScreen('zoom2.png')

    if zoom_location_active is None and zoom_location_inactive is None:
        webbrowser.open(zoom_link, new=0)

    time.sleep(30)