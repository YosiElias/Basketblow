# Imports
import pygame
import pygame as pg
from ctypes import windll

SetWindowPos = windll.user32.SetWindowPos

pg.init()
win = pg.display.set_mode((200, 30))

x, y = 100, 100
# Pin Window to the top
SetWindowPos(pygame.display.get_wm_info()['window'], -1, x, y, 0, 0, 0x0001)


#Main Loop
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
        if event.type == pg.KEYDOWN:
            SetWindowPos(pygame.display.get_wm_info()['window'], -1, x, y, 0, 0, 0x0001)
