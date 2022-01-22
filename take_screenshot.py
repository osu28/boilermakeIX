import pyautogui, time
from PIL import Image
import random

i = 21
# while (i < 40):
left = 150
top = 60
right = 350
bottom = 260

time.sleep(2)
myScreenshot = pyautogui.screenshot()
myScreenshot.crop((left, top, right, bottom)).save(r'C:\Users\zeore\Downloads\Austin, TX\Austin' + str(i) + '.png')
i += 1

