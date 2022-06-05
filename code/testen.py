import pygame
pygame.init()
font = pygame.font.Font(None, 40)

def testen(info, y = 5, x = 5):
    surface_display = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect =  debug_surf.get_rect(topleft = (x, y))
    pygame.draw.rect(surface_display, 'black', debug_rect, 1)
    surface_display.blit(debug_surf, debug_rect)