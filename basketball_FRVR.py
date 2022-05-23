import time
from PIL import Image
import webbrowser
import mss
import numpy as np
import pyautogui

width, height = pyautogui.size()
START_POINT_X = (990 / 1920) * width
START_POINT_Y = (800 / 1080) * height


outer_sq = ((471 / 1920) * width, (321 / 1080) * height)
inner_sq = ((478 / 1920) * width, (315 / 1080) * height)
sq_mid = ((639 / 1920) * width, (233 / 1080) * height)


def open_web():
    url = 'https://basketball.frvr.com/'
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
    time.sleep(3)


def take_screenshot():
    with mss.mss() as mss_obj:
        mss_obj.shot(output='screencap.png')


def execute_swipe(pos_x, pos_y):
    pyautogui.moveTo(START_POINT_X, START_POINT_Y)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(pos_x, pos_y, 0.5, button='left')  # final position
    pyautogui.mouseUp(button='left')


def update_pos(moving, t=3):
    image = get_image()
    image = get_image()
    pos_x, x1 = set_pos_x(image, x=0)
    pos_y = set_pos_y(image, y=0)
    image = get_image()
    pos_x, x2 = set_pos_x(image, x=687)
    pos_y = set_pos_y(image, y=500)
    if x1 != x2:
        moving = True
    if pos_x > START_POINT_X:
        pos_x -= (pos_x - START_POINT_X) * 0.15

    else:
        pos_x += (START_POINT_X - pos_x) * 0.15
    if moving == True:
        t = 5
        time.sleep(6.5)
    execute_swipe(pos_x, pos_y)
    moving = False
    time.sleep(t)
    return moving


def get_image():
    take_screenshot()
    image = Image.open('screencap.png')
    image = np.array(image)
    return image


def set_pos_x(image, x):
    x1 = 0
    pos_x = 0
    while x <= START_POINT_X:
        if list(image[235][x]) <= [97, 57, 46] and list(image[280][x]) >= [90, 50, 40]:
            pos_x = ( 250/ 1920) * width + x
            x1 = x
            break
        x += 1
    return pos_x, x1


def set_pos_y(image, y):
    y_pos = 0
    while y > 250:
        if list(image[y][1024]) == [97, 57, 46]:
            y_pos = y - (60 / 1080) * height
            break
        y -= 1
    return y_pos


def main_loop():
    # execute_swipe(START_POINT_X, START_POINT_Y)
    moving = False
    while True:
        moving = update_pos(moving)


if __name__ == '__main__':
    open_web()
    time.sleep(3)
    main_loop()
