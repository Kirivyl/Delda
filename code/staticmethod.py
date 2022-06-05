import pygame
import os
from Settings import *
class static(object):
    
        

    path = {}
    path['file'] = os.path.dirname(os.path.abspath(__file__))
    path['graphics'] = os.path.join(path['file'], "graphics")
    path['music'] = os.path.join(path['file'], "music")
    path['weapons'] = os.path.join(path['file'], "weapons")
    path['map'] = os.path.join(path['file'], "map")
    path['player'] = os.path.join(path['file'], "player")

    path_floor = {}
    path_floor['file'] = os.path.dirname(os.path.abspath(__file__))
    path_floor['map'] = os.path.join(path['file'], "map")

    @staticmethod
    def filepath(name):
        return os.path.join(static.path['file'], name)

    @staticmethod
    def imagepath(name):
        return os.path.join(static.path['graphics'], name)

    @staticmethod
    def floorpath(name):
        return os.path.join(static.path_floor['map'], name)

    @staticmethod
    def musicpath(name):
        return os.path.join(static.path['music'], name)

    @staticmethod
    def weaponpath(name):
        return os.path.join(static.path['weapons'], name)

    @staticmethod
    def mappath(name):
        return os.path.join(static.path['map'], name)
    
    @staticmethod
    def playerpath(name):
        return os.path.join(static.path['player'], name)

weapon = { 
        'sword': {'cooldown': 200, 'damage': 15, 'graphic': pygame.image.load(static.weaponpath('sword.png'))},
        'axe': {'cooldown': 300, 'damage': 24, 'graphic': pygame.image.load(static.weaponpath('axe.png'))},
        'katana': {'cooldown': 150, 'damage': 10, 'graphic': pygame.image.load(static.weaponpath('katana.png'))},
        'hammer': {'cooldown': 500, 'damage': 50, 'graphic': pygame.image.load(static.weaponpath('hammer.png'))},
        'bigsword': {'cooldown': 400, 'damage': 40, 'graphic': pygame.image.load(static.weaponpath('bigsword.png'))},
    }

