import pygame
from Player import *

class Weapon (pygame.sprite.Sprite):
    def __init__(self, groups, object_sprites,player ):
        super().__init__(groups)
        self.object_sprites = object_sprites
        movement = player.status('_')[0]


        self.image = pygame.Surface((40,40))#pygame.image.load('..\Delda_SpieleProgrammierung\code\graphics\weapon\weapon.png')

        if movement == 'right':

            self.rect = self.image.get_rect(center = player.rect.center)