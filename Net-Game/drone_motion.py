import cv2
from djitellopy import Tello

import time
from PIL import Image
import webbrowser
import mss
import numpy as np
import pyautogui
import serial
import serial.tools.list_ports


PORT_NUMBER = 'COM7'  # TODO change according to port number
BAUDRATE = 9600
arduino_data = serial.Serial(PORT_NUMBER, BAUDRATE)
width, height = 320, 240

# def convert_blow(drone, blow):
#     if 105000 < blow:
#         drone.flip_back()
#     drone.move_down(30)
#     time.sleep(5)


def arduino_data_function():
    if arduino_data.in_waiting:
        packet = arduino_data.readline()
        blow = packet.decode('utf').rstrip('\n')
        print(blow)
        blow = (int(blow))
        print(blow)
        return blow


if __name__ == '__main__':
    drone = Tello()
    drone.connect()
    drone.for_back_velocity = 0
    drone.left_right_velocity = 0
    drone.up_down_velocity = 0
    drone.yaw_velocity = 0
    drone.speed = 0

    drone.streamoff()
    drone.streamon()

    drone.takeoff()
    drone.move_up(30)
    time.sleep(5)
    fail = 0
    while True:
        frame_read = drone.get_frame_read()
        my_frame = frame_read.frame
        img = cv2.resize(my_frame, (width, height))
        blow = arduino_data_function() # TODO - get blow information
        if fail == 2:
            drone.land()
            break
        if blow < 103000:
            continue
        if 105000 < int(blow):
            drone.move_up(10)
            time.sleep(1)
            drone.flip_back()
            time.sleep(2)
        else:
            drone.move_down(10)
            time.sleep(5)
            fail += 1
        cv2.imshow("image", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            drone.land()
            break
    # for blow in [-1]:
    #     convert_blow(drone, blow)
    drone.land()

# rotate_clockwise (between 45 and -45 degree), rotate_counter_clockwise, flip

# rotate_clockwise (between 45 and -45 degree), rotate_counter_clockwise, flip
