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
background = pygame.image.load("images/bg.png").convert_alpha()
mapl = pygame.image.load("images/map.png").convert_alpha()

HelveticaNM = pygame.font.Font("fonts/HelveticaNeueMedium.ttf", 30)

background_width = background.get_width()
skala_width = skala.get_width()

scale = 0.45  #45%

new_width = int(periskopL.get_width() * scale)
new_height = int(periskopL.get_height() * scale)

periskop = pygame.transform.scale(periskopL, (new_width, new_height))

scale = 0.43

new_width = int(mapl.get_width() * scale)
new_height = int(mapl.get_height() * scale)

map = pygame.transform.scale(mapl, (new_width, new_height))

dist_a = 100
dist_b = 100
dist_c = 100

offset = 613
bg_offset = 613

game_state = 0

degree = 0
goal_degree = randint(0, 36) * 10
backroundx = randint(0, 900)
enemy_rect = pygame.Rect((300, 250, 200, 50))

pygame.display.set_caption("Sea Raider 2")
clock = pygame.time.Clock()

dist_a_surf = HelveticaNM.render(str(dist_a), False, (255, 255, 255))
dist_b_surf = HelveticaNM.render(str(f"{dist_b}"+"m"), False, (255, 255, 255))
dist_c_surf = HelveticaNM.render(str(dist_c), False, (255, 255, 255))




def keyboard():
    global offset, degree, bg_offset
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        pass

    if keys[pygame.K_a] and game_state == 1:
        offset -= 3
        if degree < 0:
            degree = 360
        degree -= 0.5

    if keys[pygame.K_s]:
        pass

    if keys[pygame.K_d] and game_state == 1:
        offset += 3
        if degree > 360:
            degree = 0
        degree += 0.5

    offset %= skala_width
    bg_offset %= background_width
def draw():


    game_surface.fill((255, 255, 255))
    if game_state == 0:
        game_surface.blit(map, (0, 0))
        game_surface.blit(dist_b_surf, (160, 265))



    elif game_state == 1:
        game_surface.blit(background, (-offset + backroundx, -300))
        game_surface.blit(background, (background_width - offset + backroundx, -300))
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

            if event.key == pygame.KMOD_ALT and event.key == pygame.K_F4:
                pygame.quit()
                exit()

            elif event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_CTRL:
                pass

            elif event.key == pygame.K_ESCAPE:
                game_state -= 1

            elif event.key == pygame.K_SPACE:
                if game_state == 0:
                    game_state = 1
                elif game_state == 1 and goal_degree - 5 < degree < goal_degree + 5:
                    game_state = 2




    keyboard()
    draw()
    if game_state == 1:
        print(int(degree), "°")
    elif game_state == 0:
        print(goal_degree)
    #pygame.draw.rect(game_surface, (255, 0, 0), enemy_rect)


    scaled = pygame.transform.scale(game_surface, screen.get_size())
    screen.blit(scaled, (0, 0))

    pygame.display.flip()
    clock.tick(60)