import pygame
from Player import *
from staticmethod import * 

class Weapon (pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        #self.object_sprites = object_sprites
        movement = player.status.split('_')[0]
        
        
        
        print(movement)
        #full_path = os.path.join(static.weaponpath['player'], movement)
        self.image = pygame.image.load(static.weaponpath('sword.png'))
        

        if movement == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright)
        elif movement == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft)
        elif movement == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)
        elif movement == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)
        else:
            self.rect = self.image.get_rect(center = player.rect.center)
        self.hitbox = self.rect.inflate(Settings.hitboxweapon_x, Settings.hitboxweapon_y)