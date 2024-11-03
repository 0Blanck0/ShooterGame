from bullet import Bullet

import pygame
import constant


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.health = constant.default_player_health
        self.attack = constant.default_player_attack
        self.speed = constant.default_player_speed
        self.score = 0
        self.all_bullet = pygame.sprite.Group()
        # Image for player sprite
        self.image = constant.player_image_sprite
        self.rect = self.image.get_rect()
        # Set default position on screen
        self.rect.x = (constant.screen_width / 2) - self.rect.width / 2
        self.rect.y = constant.screen_height - (265 - (self.rect.width / 4))
        self.default_rect = self.rect
        # Definition of life bar color (rgb)
        self.bar_color = (111, 210, 46)
        self.default_bar_color = (111, 210, 46)
        self.background_bar_color = (0, 0, 0)

    def update_health_bar(self, surface):
        # Definition of life bar position
        bar_position = [self.rect.x + 45, self.rect.y - 10, self.health, 5]
        background_bar_position = [self.rect.x + 45, self.rect.y - 10, constant.default_player_health, 5]
        # Draw life bar
        pygame.draw.rect(surface, self.background_bar_color, background_bar_position)
        pygame.draw.rect(surface, self.bar_color, bar_position)

    def damage(self, amount):
        if self.health > 0:
            self.health -= amount
        else:
            self.bar_color = (0, 0, 0)

        if self.health < 1:
            self.game.game_over()

    # Create new bullet in the game
    def fire(self):
        bullet = Bullet(self)
        self.all_bullet.add(bullet)

    #########
    # MOVES #
    #########

    def dont_move(self):
        self.rect.x = self.rect.x

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_mummy):
            self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed
