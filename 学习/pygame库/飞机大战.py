class settings():

    def __init__(self):

        self.screen_width=450
        self.screen_higth=600
        self.bg_color=(255,255,255)
import sys
import pygame
class Ship():
    def __init__(self,screen):
        self.screen =screen

        self.image =pygame.image.load("images.bmp")
        self.rect = self.image.get_rect()
        self .screen_rect =screen.get_rect()

        self.rect.centerx =self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)

def run_game():
    pygame.init()
    ai_settings =settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_higth))
    pygame.display.set_caption("Alien Invasion")

    ship =Ship(screen)


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
run_game()
