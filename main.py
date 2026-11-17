import settings 
import pygame

pygame.init()
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

player_x = 100
player_y = 200
snake_body = [(player_x, player_y)]
player_length = 1
score = 0
direction = "NONE"
speed= 240
dt = clock.tick(settings.FPS) / 1000

running = True
game_over = False


while running:
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_x += speed * dt

    if keys[pygame.K_LEFT]:
        player_x -= speed * dt

    if keys[pygame.K_UP]:
        player_y -= speed * dt

    if keys[pygame.K_DOWN]:
        player_y += speed * dt


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break   


    pygame.draw.rect(
        screen,
        settings.CYAN,
        (player_x,player_y,40,40)
    )            



    pygame.display.flip()
    clock.tick(settings.FPS)
pygame.quit()
#py -3.13 main.py