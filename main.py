import settings 
import pygame
import random

pygame.init()
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
arena = pygame.Rect(15, 15, 1250, 650)
player = pygame.Rect(100, 200, 40, 40)
chaser1 = pygame.Rect(800, 300, 40, 40)
coin = pygame.Rect(400, 300, 20, 20)


speed= 480
chaser1_speed = 240
score = 0
play_again_button = pygame.Rect(400, 390, 200, 60)
 

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

    if player.colliderect(coin):
        score += 1
        coin.x = random.randint(15, 1245)
        coin.y = random.randint(15, 645)

    direction = pygame.Vector2(
        player.centerx - chaser1.centerx,
        player.centery - chaser1.centery
    )  

    if direction.length() > 0:
        direction = direction.normalize() 

    chaser1.x += direction.x * chaser1_speed * dt
    chaser1.y += direction.y * chaser1_speed * dt

    if game_over:

        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        play_again_text = font.render("PLAY AGAIN", True, (0, 0, 0))

        screen.blit(game_over_text, (400, 280))
        screen.blit(final_score_text, (400, 330))

        pygame.draw.rect(screen, (0, 255, 0), play_again_button)
        screen.blit(play_again_text, (415, 408))
        


    pygame.draw.rect(screen, settings.CYAN, player)
    pygame.draw.rect(screen, settings.RED, chaser1)
    pygame.draw.rect(screen, settings.GOLD, coin)

    pygame.draw.rect(screen, settings.WHITE, arena, 3)
    score_text = font.render(f"Score: {score}", True, settings.WHITE)
    screen.blit(score_text, (30, 30))
    pygame.display.flip()
pygame.quit()
print(direction)
#py -3.13 main.py