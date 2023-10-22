import time
import random
import ctypes

def msgbox(message = "关注GMEnglish喵，关注GMEnglish谢谢喵", title = "广告"):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)

while True:
    waitSecond = random.randint(60, 600)
    time.sleep(waitSecond)
    msgbox()
