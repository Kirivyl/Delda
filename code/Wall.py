import pygame
from Settings import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, position, groups, sprite_art, surface = pygame.Surface((TEST_SIZE, TEST_SIZE))):
        super().__init__(groups)
        
        self.position = position
        self.sprite_art = sprite_art  
        self.image = surface     
        #self.image = pygame.image.load(Settings.imagepath('wall_bricks.png')).convert_alpha() # Bild in ordnerstruktur
        #self.image = pygame.transform.scale(self.image, Settings.tile_size) # Bild skalieren
        if sprite_art == 'grass':
            self.rect = self.image.get_rect(topleft = (position[0], position[1] - TEST_SIZE))
        else:    
            self.rect = self.image.get_rect(topleft = position) # Position des Bildes
        self.mask = pygame.mask.from_surface(self.image)
        self.hitbox = self.rect.inflate(Settings.hitboxwall_x, Settings.hitboxwall_y)


