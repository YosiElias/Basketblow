import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
info = pygame.display.Info()

SIZE = WIDTH, HEIGHT = info.current_w, info.current_h

# throw types:
TOO_WEAK_x2 = 0  # "to_weak_x2"
TOO_WEAK_x1 = 1  # "to_weak_x1"
TOO_WEAK = 2  # "to_weak
PERFECT = 3  # "perfect"
TOO_STRONG = 4  # "to_strong"
