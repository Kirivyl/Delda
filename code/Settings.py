import pygame 
import os
from staticmethod import * 

class Settings(object):
    
    window = {'width': 1600, 'height': 800}
    floor = {'width': 8448, 'height': 6912} # 8448, 6912
    fps = 60
    title= 'Delda'
    # wall Settings

    tile_size =  32,32
    tile_pos = (0, 0)

    # TEST_SIZE = 64,64

    hitboxwall_x = 0
    hitboxwall_y = -20
    # player Settings
    player_size = 64,64
    player_pos = (0,0) 
    player_speed = 3
    # Attack
    attacking_cooldown = 500


    # Animations 

    #frame_index = 0
    animation_speed  = 0.1

    hitboxplayer_x = 1
    hitboxplayer_y = 26

    directon_x = 0
    directon_y = -18

    # Weapon
    hitboxweapon_x = 0
    hitboxweapon_y = 0

   
    # Kamera Settings für denn Y-Kamera und X-Kamera


    # y_camera_pos_y = 200
    # y_camera_pos_x = 100


    # global path
    # path = {}
    # path['file'] = os.path.dirname(os.path.abspath(__file__))
    # path['graphics'] = os.path.join(path['file'], "graphics")
    # path['music'] = os.path.join(path['file'], "music")
    # path['weapons'] = os.path.join(path['file'], "weapons")
    # path['map'] = os.path.join(path['file'], "map")
    # path['player'] = os.path.join(path['file'], "player")

    # path_floor = {}
    # path_floor['file'] = os.path.dirname(os.path.abspath(__file__))
    # path_floor['map'] = os.path.join(path['file'], "map")

    # @staticmethod
    # def filepath(name):
    #     return os.path.join(path['file'], name)

    # @staticmethod
    # def imagepath(name):
    #     return os.path.join(path['graphics'], name)

    # @staticmethod
    # def floorpath(name):
    #     return os.path.join(Settings.path_floor['map'], name)

    # @staticmethod
    # def musicpath(name):
    #     return os.path.join(path['music'], name)

    # @staticmethod
    # def weaponpath(name):
    #     return os.path.join(path['weapons'], name)

    # @staticmethod
    # def mappath(name):
    #     return os.path.join(path['map'], name)
    
    # @staticmethod
    # def playerpath(name):
    #     return os.path.join(path['player'], name)

    # weapon = { 
    #     'sword': {'cooldown': 200, 'damage': 15, 'graphic': weaponpath('sword.png')},
    #     'axe': {'cooldown': 300, 'damage': 24, 'graphic': weaponpath('axe.png')},
    #     'katana': {'cooldown': 150, 'damage': 10, 'graphic': weaponpath('katana.png')},
    #     'hammer': {'cooldown': 500, 'damage': 50, 'graphic': weaponpath('hammer.png')},
    #     'bigsword': {'cooldown': 400, 'damage': 40, 'graphic': weaponpath('bigsword.png')},
    # }
     # HUD
    bar_height = 20
    health_bar_width = 100
    energy_bar_width = 70
    item_box_size = 50
    hud_font = static.imagepath('font.ttf')


    hud_font_size = 20
        
    water_color = '#00FFFF'
    hud_bg_color = '#000000'
    hud_border_color =  '#FFFFFF'
    text_color = '#AAAAAA'

    health_color = 'red'
    energy_color = 'blue'
    hud_border = 'gold'

# weapon = { 
#         'sword': {'cooldown': 200, 'damage': 15, 'graphic': pygame.image.load(Settings.weaponpath('sword.png'))},
#         'axe': {'cooldown': 300, 'damage': 24, 'graphic': pygame.image.load(Settings.weaponpath('axe.png'))},
#         'katana': {'cooldown': 150, 'damage': 10, 'graphic': pygame.image.load(Settings.weaponpath('katana.png'))},
#         'hammer': {'cooldown': 500, 'damage': 50, 'graphic': pygame.image.load(Settings.weaponpath('hammer.png'))},
#         'bigsword': {'cooldown': 400, 'damage': 40, 'graphic': pygame.image.load(Settings.weaponpath('bigsword.png'))},
#     }


WORLD_MAP = [                                                                               # Map render
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]
#print(WORLD_MAP)

TEST_SIZE = 32
