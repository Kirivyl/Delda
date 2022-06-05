from this import d
import pygame
from Settings import *
from staticmethod import * 

class HUD():
    def __init__(self):        
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(Settings.hud_font, Settings.hud_font_size)
        self.health_bar_rect = pygame.Rect(15, Settings.bar_height, Settings.health_bar_width, Settings.bar_height)
        self.energy_bar_rect = pygame.Rect(15, Settings.bar_height + 15, Settings.energy_bar_width, Settings.bar_height)

    def display(self, player):
        pygame.draw.rect(self.display_surface, (0,0,0), self.health_bar_rect)