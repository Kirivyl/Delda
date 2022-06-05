# Inspiration https://www.youtube.com/watch?v=QU1pPzEGrqw&t=289s
# Ich habe das video als Inspiration und Hilfe genommen ich fande die Idee cool und hab die selben Techniken auf eigener weiße angewendet
# music: DOOM_Enternal Theme

from numpy import full
import pygame, sys 
from Settings import *  # import all Settings from Settings.py
from testen import * # import debug from debug.py
from Level import * # import level from level.py
from fullscreen import * # import fullscreen from fullscreen.py
from win32api import GetSystemMetrics
from support import*
from pygame import*


class Delda:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption(Settings.title)
        self.screen = pygame.display.set_mode((Settings.window['width'], Settings.window['height']))
        self.clock = pygame.time.Clock()

        self.level =  Level()
        self.level.map()

        mixer.init
        pygame.mixer.music.load(Settings.musicpath('music.wav'))
        pygame.mixer.music.play(-1)
        

    
        self.volume = 0.3
        self.music_louder = pygame.mixer.music.set_volume(self.volume + 0.1)
        self.music_quiter = pygame.mixer.music.set_volume(self.volume -0.1)

        #aself.level.cam()

    # def vollbild(self):
    #      fullscreen = False

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
                    elif event.key == pygame.K_KP_MINUS:
                        pygame.mixer.music.set_volume(self.volume -0.1)
            #         if fullscreen:
            #              screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
            #         else:
            #              screen = pygame.display.set_mode((640, 480), 0, 32)
            # 


            self.screen.fill('Black')
            #debug('Delda')
            self.level.run()
            self.clock.tick(Settings.fps)   #Fps is set in Settings.py
            #self.level.cam()
            #player.update()
            pygame.display.update()

    #def draw(self):
        #self.level.draw(self.screen)


if __name__ == '__main__':
    game = Delda()
    game.run()
