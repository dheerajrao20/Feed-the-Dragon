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

background_image = pygame.transform.scale( pygame.image.load(GAME_FOLDER + 'dragon_night.jpg'), (WINDOW_WIDTH, WINDOW_HEIGHT))

#Game Actors
dragon = pygame.image.load(GAME_FOLDER + 'dragon.png')
# dragon_x = WINDOW_WIDTH - 80
# dragon_y = 100
dragon_rect = dragon.get_rect()
dragon_rect.left = 0
dragon_rect.right = 400
dragon_velocity = 5
s
# adding coin
coin = pygame.image.load(GAME_FOLDER + 'coin.png')
# coin_x = 0
# coin_y = 100
coin_rect = coin.get_rect()
coin_rect.left = 0
coin_rect.right = 400



#main game loop (life of the game)
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    #listen to the events (user actions)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    #know the keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dragon_y > 100:
        dragon_y -= dragon_velocity
    elif keys[pygame.K_DOWN] and dragon_y < WINDOW_HEIGHT - 64:
        dragon_y += dragon_velocity


    #apply the background
    display_surface.blit(background_image, (0,0))

    #draw the actors
    display_surface.blit(dragon, (dragon_x,dragon_y))
    #refesh the window
    pygame.display.update()

    #moderate the rate of iteration
    #By this the game runs at the same speed over different CPU's
    #Also cooperative multi tasking is achieved
    clock.tick(FPS)

#deallocate the resources
pygame.quit()