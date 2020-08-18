import pygame
import constant
import game

screen_width = constant.screen_width
screen_height = constant.screen_height
background = constant.background_default

lastDir = "Right"
running = True

pygame.init()

# Generate screen of game

pygame.display.set_caption(constant.game_name)
screen = pygame.display.set_mode((screen_width, screen_height))

game_var = game.Game()

while running:

    # Apply background to game
    screen.blit(background, (0, -200))

    # Apply player sprite in game
    screen.blit(game_var.player.image, game_var.player.rect)
    game_var.player.update_health_bar(screen)

    # Apply monsters sprite in game
    game_var.all_mummy.draw(screen)

    # Get all bullet and move it
    for bullets in game_var.player.all_bullet:
        bullets.move()

    # Get all monsters sprite in game
    for monster in game_var.all_mummy:
        monster.forward()
        monster.update_health_bar(screen)

    # Apply bullet
    game_var.player.all_bullet.draw(screen)


    # Check player direction
    if game_var.pressed.get(pygame.K_RIGHT) and game_var.pressed.get(pygame.K_LEFT):
        game_var.player.nothing_move()
    elif game_var.pressed.get(pygame.K_RIGHT) and game_var.player.rect.x + (game_var.player.rect.width - 20) < screen.get_width():
        game_var.player.move_right()
        lastDir = "Right"
    elif game_var.pressed.get(pygame.K_LEFT) and game_var.player.rect.x > -20:
        lastDir = "Left"
        game_var.player.move_left()

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
            # Fire ball in press space
            if event.key == pygame.K_SPACE:
                game_var.player.fire(lastDir)
        # Disable press key
        elif event.type == pygame.KEYUP:
            game_var.pressed[event.key] = False