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
    hitboxwall_x = 0
    hitboxwall_y = -20

    # player Settings
    player_size = 64,64
    player_pos = (0,0) 
    player_speed = 3
    hitboxplayer_x = 1
    hitboxplayer_y = 26

    # Attack
    attacking_cooldown = 500

    # Animations 
    animation_speed  = 0.1
    directon_x = 0
    directon_y = -18

    # Weapon
    hitboxweapon_x = 0
    hitboxweapon_y = 0

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

TEST_SIZE = 32
