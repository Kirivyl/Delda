import pygame, sys
from pygame.locals import *
from win32api import GetSystemMetrics

class fullscreen():
    def vollbild(screen):
        screen = pygame.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)))
