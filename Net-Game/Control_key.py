import time

import pyautogui
from pynput import keyboard
from pynput.keyboard import Key, Controller
# import serial
# import serial.tools.list_ports
from basketball_FRVR import arduino_data_function

# PORT_NUMBER = 'COM7'  # TODO change according to port number
# BAUDRATE = 9600
# arduino_data = serial.Serial(PORT_NUMBER, BAUDRATE)

control = Controller()


# def convert_blow(blow):
#     if 102000 < blow < 103000:
#         blow = 0
#     elif 103000 < blow < 104000:
#         blow = 1
#     elif 104000 < blow < 104500:
#         blow = 2
#     elif 104500 < blow < 105000:
#         blow = 3
#     elif 105000 < blow:
#         blow = 4
#     else:
#         blow = -1
#     return blow

# def arduino_data_function():
#     if arduino_data.in_waiting:
#         packet = arduino_data.readline()
#         blow = packet.decode('utf').rstrip('\n')
#         if blow == None:
#             blow = -1
#         blow = convert_blow(int(blow))
#         if blow == None:
#             return -1
#         print(blow)
#         return blow



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
        # control.press(keyboard.Key.alt)
        # time.sleep(.2)
        # control.press(keyboard.Key.tab, 3)
        # control.release(keyboard.Key.tab, 3)
        # time.sleep(.2)
        # control.release(keyboard.Key.alt)
        return False
def main_key():
    blow = arduino_data_function()
    time.sleep(5)
    control.press(Key.space)
    # time.sleep(10)
    control.release(Key.space)
    if blow ==None:
        blow=-1
    if blow > 0:
        control.press(Key.space)
        # time.sleep(10)
        control.release(Key.space)
    # # Collect events until released
    # with keyboard.Listener(
    #         on_press=on_press,
    #         on_release=on_release) as listener:
    #     listener.join()
