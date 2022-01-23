from telnetlib import EC

import pyautogui, time
from selenium import webdriver
import os
from time import sleep
from PIL import Image
import random

# assign url in the webdriver object
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
folder_path = 'C:/Users/asus/boilermakeIX/cities'

locations = {"new_york_city" : "https://earth.google.com/web/search/New+York+City/@40.69748804,-73.97968093,1.77977873a,112809.08686305d,35y,0h,0t,0r/data=CigiJgokCZgbafYiO0NAEZgbafYiO0PAGb-caIvkjkBAIcYsJtAAlFTA",
             "austin" : "https://earth.google.com/web/search/Austin/@30.3077609,-97.7534014,189.91006509a,64223.29326712d,35y,0h,0t,0r/data=CigiJgokCX2Yn8Hlez5AEYffYwhOHj5AGekpuPjLYVjAIQlH11ixfljA"}
cities = ["new_york_city", "austin"]
# def searchplace():
    # search_bar = driver.find_element_by_class_name("tactile-searchbox-input")
    # search_bar.send_keys("New York City" + "\n")

    # map_options = driver.find_element_by_id("map-style")
    # map_options.click()

# searchplace()

def screenshot(num_pics, city):
    left = 400
    top = 300
    right = 1600
    bottom = 1000
    for i in range(0, num_pics):
        left_new = left + random.randint(0, 300)
        top_new = top + random.randint(0, 100)
        right_new = right - random.randint(0, 300)
        bottom_new = bottom - random.randint(0, 200)

        myScreenshot = pyautogui.screenshot()
        myScreenshot.crop((left_new, top_new, right_new, bottom_new)).save(r'C:\Users\asus\boilermakeIX\cities' + '/' + city + '/' + city + str(i) + '.png')


driver.get("https://earth.google.com/web/@34.07944953,-96.47217207,268.58712169a,9158613.20030809d,35y,0h,0t,0r")
time.sleep(15)
for city in cities:
    driver.get(locations[city])
    os.makedirs(folder_path + "/" + city, exist_ok=False)
    time.sleep(15)
    screenshot(100, city)
driver.quit()