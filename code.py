import pygame # pip install pygame
import random

#initialize the pygame framework
pygame.init()

#Create a window (display surface)
GAME_FOLDER = 'C:/Users/91870/OneDrive/Desktop/Feed-the-Dragon/'
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Apply the caption, set the icon, set the background image
pygame.display.set_caption('Feed the Dragon')

#game_icon = pygame.image.load(GAME_FOLDER + 'game_icon.ico')
#pygame.display.set_icon(game_icon)

background_image = pygame.transform.scale( pygame.image.load(GAME_FOLDER + 
'dragon_night.jpg'), (WINDOW_WIDTH, WINDOW_HEIGHT))

#Game Actors
dragon = pygame.image.load(GAME_FOLDER + 'dragon.png')
dragon_rect = dragon.get_rect()
dragon_rect.right = WINDOW_WIDTH - 10
dragon_rect.centery = WINDOW_HEIGHT//2
dragon_velocity = 5

coins = []
for i in range(6):
    coins.append(pygame.transform.scale( pygame.image.load(GAME_FOLDER + 'coin/' + str(i)+ '.png'), (32,32)))
coin_index = 0
coin_rect = coins[coin_index].get_rect()
coin_rect.left = 0
coin_rect.top = 400
coin_velocity = 5

#Game Sounds
loss = pygame.mixer.Sound(GAME_FOLDER + 'loss.wav')
loss.set_volume(0.5)
pick = pygame.mixer.Sound(GAME_FOLDER + 'pickup.wav')
pick.set_volume(0.5)
background_music = pygame.mixer.music.load(GAME_FOLDER+ 'background_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#Game HUD
#load the font and colors
big_game_font = pygame.font.Font(GAME_FOLDER + 'AttackGraffiti.ttf', 60)
small_game_font = pygame.font.Font(GAME_FOLDER + 'AttackGraffiti.ttf', 40)
GREEN = pygame.Color(0,200,0)
RED = pygame.Color(255,0,0)
WHITE = pygame.Color(255,255,255)

#render text using the font and color
title = big_game_font.render('Feed The Dragon', True, GREEN)
title_rect = title.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.top = 10

player_score = 0
player_lives = 3
score = small_game_font.render('Score: '+ str(player_score), True, WHITE)
score_rect = score.get_rect()
score_rect.left = 50
score_rect.top = 10

lives = small_game_font.render('Lives: '+ str(player_lives), True, WHITE)
lives_rect = lives.get_rect()
lives_rect.right = WINDOW_WIDTH - 50
lives_rect.top = 10

game_over_text = big_game_font.render('GAME OVER!', True, RED)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

game_restart_text = small_game_font.render('r: restart ', True, GREEN)
game_restart_text_rect = game_restart_text.get_rect()
game_restart_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50)

game_quit_text = small_game_font.render('q: quit ', True, WHITE)
game_quit_text_rect = game_quit_text.get_rect()
game_quit_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 +100)




#main game loop (life of the game)
game_status = 1
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    #listen to the events (user actions)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_q:
                running = False
            elif ev.key == pygame.K_r:
                player_score = 0
                player_lives = 3
                pygame.mixer.music.play(-1)
                coin_index = 0
                coin_rect.left = 0
                coin_rect.top = 400
                coin_velocity = 5
                dragon_rect.centery = WINDOW_HEIGHT // 2
                score = small_game_font.render('Score: ' + str(player_score), True, WHITE)
                lives = small_game_font.render('Lives: ' + str(player_lives), True, WHITE)
                game_status = 1

    #apply the background
    display_surface.blit(background_image, (0,0))

    if game_status == 1:
        #know the keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and dragon_rect.top > 100:
            dragon_rect.top -= dragon_velocity
        elif keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT :
            dragon_rect.top += dragon_velocity

        #update the coin position
        coin_rect.right+= coin_velocity

        #check whether dragon ate it
        if coin_rect.colliderect(dragon_rect):
            pick.play()
            coin_velocity+=0.5
            coin_rect.left = -150
            coin_rect.top = random.randint(100, WINDOW_HEIGHT - coin_rect.height)
            player_score+=1
            score = small_game_font.render('Score: ' + str(player_score), True, WHITE)

        #check for loss
        if coin_rect.right > WINDOW_WIDTH:
            loss.play()
            coin_rect.left = -150
            coin_rect.top = random.randint(100, WINDOW_HEIGHT- coin_rect.height)
            coin_velocity = 5
            player_lives -=1
            if player_lives > 1:
                lives = small_game_font.render('Lives: ' + str(player_lives), True, WHITE)
            elif player_lives == 1:
                lives = small_game_font.render('Lives: ' + str(player_lives), True, RED)
            elif player_lives == 0:
                game_status = 2
                pygame.mixer.music.stop()

        #draw the actors
        display_surface.blit(dragon, dragon_rect)
        display_surface.blit(coins[int(coin_index)], coin_rect)
        coin_index = (coin_index +0.2) % 6

    elif game_status == 2:
        display_surface.blit(game_over_text, game_over_text_rect)
        display_surface.blit(game_restart_text, game_restart_text_rect)
        display_surface.blit(game_quit_text, game_quit_text_rect)

    #draw the HUD
    display_surface.blit(title, title_rect)
    display_surface.blit(score, score_rect)
    display_surface.blit(lives, lives_rect)

    #refesh the window
    pygame.display.update()

    #moderate the rate of iteration
    #By this the game runs at the same speed over different CPU's
    #Also cooperative multi tasking is achieved
    clock.tick(FPS)

#deallocate the resources
pygame.quit()