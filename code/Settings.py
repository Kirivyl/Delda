import pygame as pg
import os


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

 # floor settings
    # floor_sizex = 25000
    # floor_sizey = 20000
    # def floorsize(self):
    #     while True:
    #         if Settings.floor_sizex <= 33792:
    #             Settings.floor_sizex += 1000
    #         if Settings.floor_sizey <= 27648:
    #             Settings.floor_sizey += 1000
    #         else:
    #             pass



    # Kamera Settings für denn Y-Kamera und X-Kamera


    # y_camera_pos_y = 200
    # y_camera_pos_x = 100


    weapon = { 
        'sword': {'cooldown': 200, 'damage': 15, 'graphic': '../graphics/weapons/sword/sword.png'},
        'axe': {'cooldown': 300, 'damage': 24, 'graphic': '../graphics/weapons/axe/axe.png'},
        'katana': {'cooldown': 150, 'damage': 10, 'graphic': '../graphics/weapons/katana/katana.png'},
        'hammer': {'cooldown': 500, 'damage': 50, 'graphic': '../graphics/weapons/hammer/hammer.png'},
        'bigsword': {'cooldown': 400, 'damage': 40, 'graphic': '../graphics/weapons/bigsword/bigsword.png'},
    }

    path = {}
    path['file'] = os.path.dirname(os.path.abspath(__file__))
    path['graphics'] = os.path.join(path['file'], "graphics")


    path_floor = {}
    path_floor['file'] = os.path.dirname(os.path.abspath(__file__))
    path_floor['map'] = os.path.join(path['file'], "map")

    @staticmethod
    def filepath(name):
        return os.path.join(Settings.path['file'], name)

    @staticmethod
    def imagepath(name):
        return os.path.join(Settings.path['graphics'], name)

    @staticmethod
    def floorpath(name):
        return os.path.join(Settings.path_floor['map'], name)

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
