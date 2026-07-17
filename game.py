from random import randint

import pygame
from sys import exit

from pygame.display import update

pygame.init()
pygame.mixer.init()


WIDTH = 901
HEIGHT = 557

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
game_surface = pygame.Surface((WIDTH, HEIGHT))

skala = pygame.image.load("images/gradskala.png").convert_alpha()
periskopL = pygame.image.load("images/periskop.png").convert_alpha()
skala_width = skala.get_width()

scale = 0.45  #45%

new_width = int(periskopL.get_width() * scale)
new_height = int(periskopL.get_height() * scale)

periskop = pygame.transform.scale(periskopL, (new_width, new_height))

offset = 613
degree = 0
goal_degree = randint(0, 3)

enemy_rect = pygame.Rect((300, 250, 200, 50))

pygame.display.set_caption("Sea Raider 2")
clock = pygame.time.Clock()

game_state = 0



def keyboard():
    global offset, degree
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        pass

    if keys[pygame.K_a]:
        offset -= 3
        if degree < 0:
            degree = 360
        degree -= 0.5

    if keys[pygame.K_s]:
        pass

    if keys[pygame.K_d]:
        offset += 3
        if degree > 360:
            degree = 0
        degree += 0.5

    offset %= skala_width
def draw():


    game_surface.fill((255, 255, 255))
    game_surface.blit(skala, (-offset, -300))
    game_surface.blit(skala, (skala_width - offset, -300))
    game_surface.blit(periskop, (-35, -10))

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(
                (event.w, event.h),
                pygame.RESIZABLE
            )

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            elif event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_CTRL:
                pass

            elif event.key == pygame.K_SPACE:
                pass



    keyboard()
    draw()
    print(int(degree), "°")
    #pygame.draw.rect(game_surface, (255, 0, 0), enemy_rect)


    scaled = pygame.transform.scale(game_surface, screen.get_size())
    screen.blit(scaled, (0, 0))

    pygame.display.flip()
    clock.tick(60)