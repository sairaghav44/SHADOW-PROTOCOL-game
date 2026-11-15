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


running = True
game_over = False


while running:
    screen.fill((0, 0, 0))

    if direction == "RIGHT":
     player_x = player_x +40
    if player_x >= screen.get_width() -4:
        player_x = screen.get_width() -4

    if direction == "LEFT":
     player_x = player_x - 4
     if player_x <= 0:
        player_x = 0

    if direction == "UP":
         player_y = player_y - 4
         if player_y <= 0:
            player_y = 0

    if direction == "DOWN":
     player_y = player_y +40
     if player_y >= screen.get_height() -4:
        player_y = screen.get_height() -4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break   

        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_RIGHT:
                  direction = "RIGHT"
        
            if event.key == pygame.K_LEFT:
                  direction = "LEFT"
        
            if event.key == pygame.K_UP:
                 direction = "UP"
        
            if event.key == pygame.K_DOWN:
                 direction = "DOWN"

                 
    pygame.draw.rect(
        screen,
        settings.CYAN,
        (player_x,player_y,40,40)
    )            



    pygame.display.flip()
    clock.tick(settings.FPS)
pygame.quit()
#py -3.13 main.py