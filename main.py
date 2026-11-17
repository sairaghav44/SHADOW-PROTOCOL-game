import settings 
import pygame

pygame.init()
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
arena = pygame.Rect(15, 15, 1250, 650)
player = pygame.Rect(100, 200, 40, 40)
chaser = pygame.Rect(800, 300, 40, 40)

player_x = 100
player_y = 200
chaser_x = 800
chaser_y = 300
player_body = [(player_x, player_y)]
player_length = 1
score = 0
direction = "NONE"
speed= 480
 

running = True
game_over = False


while running:
    dt = clock.tick(settings.FPS) / 1000

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.x += speed * dt
    
    if keys[pygame.K_LEFT]:
        player.x -= speed * dt

    if keys[pygame.K_UP]:
        player.y -= speed * dt

    if keys[pygame.K_DOWN]:
        player.y += speed * dt

# LEFT
    if player.left < arena.left:
        player.left = arena.left

# RIGHT
    if player.right > arena.right:
        player.right = arena.right

# TOP
    if player.top < arena.top:
        player.top = arena.top

# BOTTOM
    if player.bottom > arena.bottom:
        player.bottom = arena.bottom


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break   

            # Apple collision
    player_rect = pygame.Rect(player_x, player_y, 40, 40)
    chaser_rect = pygame.Rect(chaser_x, chaser_y, 40, 40)

    if player.colliderect(chaser):

            chaser = chaser()
            chaser_x, chaser_y = chaser

            print("PLAYER CAUGHT!!!!!!!!!!")


    pygame.draw.rect(screen, settings.CYAN, player)
    pygame.draw.rect(screen, settings.RED, chaser)

    pygame.draw.rect(screen, settings.WHITE, arena, 3)

    pygame.display.flip()
pygame.quit()
#py -3.13 main.py