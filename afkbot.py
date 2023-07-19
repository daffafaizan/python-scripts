import pyautogui as pag
import random
import time

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)
    time.sleep(60)

# https://youtube.com/shorts/A6AUTu6Pju4?feature=share