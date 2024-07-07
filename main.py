import pygame
import math
import constant
import game

screen_width = constant.screen_width
screen_height = constant.screen_height
background = constant.background_default

banner = constant.banner_default
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()

lastDir = "Right"
running = True

pygame.init()

# Generate screen of game

pygame.display.set_caption(constant.game_name)
screen = pygame.display.set_mode((screen_width, screen_height))

banner_rect.x = math.ceil(screen.get_width() / 4)
banner_rect.y = math.ceil(screen.get_height() / 4 - 100)

# Generate button
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 1.6)

game_var = game.Game()

while running:

    # Apply background to game
    screen.blit(background, (0, -200))

    # Start game if is_playing is true
    if game_var.is_playing:
        game_var.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Update screen of game
    pygame.display.flip()

    # Get all event
    for event in pygame.event.get():
        # Exit event
        if event.type == pygame.QUIT:
            # Exit game
            running = False
            pygame.quit()
        # Check press key of keyboard
        elif event.type == pygame.KEYDOWN:
            # Save actual press key
            game_var.pressed[event.key] = True
            # Fireball in press space
            if event.key == pygame.K_SPACE:
                game_var.player.fire(lastDir)
        # Disable press key
        elif event.type == pygame.KEYUP:
            game_var.pressed[event.key] = False
        # Detection event mouse down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game_var.start_game()
