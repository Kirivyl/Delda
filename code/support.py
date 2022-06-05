from csv import reader
from os import walk 
import pygame
from Settings import Settings

def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        layout = reader(map,delimiter = ',')
        for row in layout: 
            terrain_map.append(row)
        return terrain_map

def import_folder(path):
    surface_list = []
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path =path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf, Settings.player_size)
            surface_list.append(image_surf)
            #print(full_path)  
    return surface_list
