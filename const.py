import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
info = pygame.display.Info()

SIZE = WIDTH, HEIGHT = info.current_w, info.current_h

# throw types:
TOO_WEAK = 0  # "to_weak"
TOO_WEAK_x2 = 1  # "to_weak_x2"
PERFECT = 2  # "perfect"
TOO_STRONG = 3  # "to_strong"
TOO_STRONG_x2 = 4  # "to_strong_x2"
