import pyautogui
from colorama import Fore

count = 0
def click(x):
    pyautogui.click(x)
    print(Fore.YELLOW, pyautogui.position(), screen.getpixel(coords), "BANG",count)
while True:
    count += 1
    try:
        screen = pyautogui.screenshot()
        coords = pyautogui.position()
        colors = (156,154,154)
        if screen.getpixel(coords) == colors:
            click(coords)
        print(Fore.WHITE, pyautogui.position(), screen.getpixel(coords),count)  
    except IndexError:
        print(Fore.GREEN +"IndexError: Out of range, Cursor Not Found" ,count)


#CSGO AIM MAP colors = (4, 49, 96)
#3, 212, 3
#4, 46, 91
#177, 205, 232