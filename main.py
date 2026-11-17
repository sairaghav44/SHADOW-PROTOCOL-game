import settings 
import pygame

pygame.init()
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
arena = pygame.Rect(15, 15, 1250, 650)
player = pygame.Rect(100, 200, 40, 40)
chaser1 = pygame.Rect(800, 300, 40, 40)


speed= 480
chaser1_speed = 350
 

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

    

    if player.colliderect(chaser1):
        game_over= True
        print("PLAYER CAUGHT!!!!!!!!!!")
        running = False

    direction = pygame.Vector2(
        player.centerx - chaser1.centerx,
        player.centery - chaser1.centery
    )  

    if direction.length() > 0:
        direction = direction.normalize() 

    chaser1.x += direction.x * chaser1_speed * dt
    chaser1.y += direction.y * chaser1_speed * dt


    pygame.draw.rect(screen, settings.CYAN, player)
    pygame.draw.rect(screen, settings.RED, chaser1)

    pygame.draw.rect(screen, settings.WHITE, arena, 3)

    pygame.display.flip()
pygame.quit()
print(direction)
#py -3.13 main.py