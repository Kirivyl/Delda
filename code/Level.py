import pygame
from Settings import *
from Wall import *
from Player import *
from testen import *
from support import*
from random import*
from Weapon import *
from hud import *
from staticmethod import * 

class Level:
    def __init__(self):

        # Display draw und die Sprites werden geladen
        self.surface_display = pygame.display.get_surface()
        self.object_sprites = YCameraGroupe()  # pygame.sprite.Group()
        self.touch_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.weapon_sprite = pygame.sprite.Group()
        self.map()
        #HUD
        self.hud = HUD()

    def map(self):
        layouts = {
            'border': import_csv_layout(static.mappath('Delda_border.csv')),
            'object': import_csv_layout(static.mappath('Delda_objecte.csv')),
            'floor': import_csv_layout(static.mappath('Delda_floor.csv'))
        }
        graphics = {
            'grass': import_folder('..\Delda_Entwicklung\code\graphics\grass'),

        }
        print(graphics)
        for boundary, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TEST_SIZE
                        y = row_index * TEST_SIZE
                        if boundary == 'border':
                            Wall((x, y), [self.object_sprites], 'invisble')
                        if boundary == 'floor':
                            pass
        self.player = Player((8000, 4500), self.object_sprites, self.player_sprite, self.attack)

    def attack(self):
            Weapon(self.player, self.weapon_sprite)


    def run(self):  # run the level
        self.hud.display(self.surface_display)
        self.object_sprites.custom_draw(self.player)  # draw the sprites
        self.touch_sprites.draw(self.surface_display)
        self.weapon_sprite.draw(self.surface_display)
        self.weapon_sprite.update()
        self.touch_sprites.update()
        self.object_sprites.update()
        self.player_sprite.update()

class YCameraGroupe(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.halber_screen_breite = self.display_surface.get_size()[0] // 2
        self.halber_screen_hoehe = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.floor_surface = pygame.image.load(static.floorpath('..\map\Delda.png')).convert()
        self.floor_surface = pygame.transform.scale(self.floor_surface,(Settings.floor['width']*2, Settings.floor['height']*2))
        self.floor_rect = self.floor_surface.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.halber_screen_breite
        self.offset.y = player.rect.centery - self.halber_screen_hoehe
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)
        # Player Draw
        offset_pos = player.rect.topleft - self.offset
        self.display_surface.blit(player.image, offset_pos)

