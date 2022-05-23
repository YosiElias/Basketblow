import time

from pynput import keyboard
from pynput.keyboard import Key, Controller

control = Controller()

def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
        if key.char == 'p':
            print("pppp")
            control.press(Key.space)
            # time.sleep(10)
            control.release(Key.space)
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

def on_release(key):
    print('Key released: {0}'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
def main_key():
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

# # time.sleep(5)
# # Press and release
# control.press(Key.space)
# # time.sleep(10)
# control.release(Key.space)
#
# # from pynput.keyboard import Key, Controller
# #
# # control = Controller()
# #
# # # Press and release space
# # control.press(Key.space)
# # control.release(Key.space)