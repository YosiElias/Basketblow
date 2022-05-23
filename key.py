import time

from pynput import keyboard
# import keyword
from pynput.mouse import Button, Controller
# from pynput.mouse import Key

mouse = Controller()
# print("pppp")
# _keyboard.press(Button.left)
# _keyboard.release(Button.left)
def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
        if key.char == 'p':
            print("pppp")
            mouse.press(Button.left)
            # time.sleep(10)
            mouse.release(Button.left)
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

def on_release(key):
    print('Key released: {0}'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

time.sleep(5)
# Press and release
mouse.press(Button.left)
# time.sleep(10)
mouse.release(Button.left)