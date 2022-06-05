# Inspiration https://www.youtube.com/watch?v=QU1pPzEGrqw&t=289s
# Ich habe das video als Inspiration und Hilfe genommen ich fande die Idee cool und hab die selben Techniken auf eigener weiße angewendet
# music: DOOM_Enternal Theme

from numpy import full
import pygame, sys 
from Settings import *  
from testen import * 
from Level import * 
from fullscreen import * 
from support import*
from pygame import*
from staticmethod import * 


class Delda:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption(Settings.title)
        self.screen = pygame.display.set_mode((Settings.window['width'], Settings.window['height']))
        self.clock = pygame.time.Clock()
        self.level =  Level()
        self.level.map()
        self.volume = 0.2
        mixer.init
        pygame.mixer.music.load(static.musicpath('music.wav'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.volume)
        

    def run(self):
        while True:
            for event in pygame.event.get():   
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_KP_PLUS:            
                        pygame.mixer.music.set_volume(self.volume +0.1)
                        print(self.volume)
                    elif event.key == pygame.K_KP_MINUS:
                        pygame.mixer.music.set_volume(self.volume -0.1)
                        print(self.volume)
            self.screen.fill('Black')
            self.level.run()
            self.clock.tick(Settings.fps)   #Fps is set in Settings.py
            pygame.display.update()
if __name__ == '__main__':
    game = Delda()
    game.run()
