import pygame
import constant
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        # Default health point of mummy
        self.health = 100
        self.max_health = 100
        # Default attack point of mummy
        self.attack = 0.1
        # Default kill point
        self.kill_point = 2 + random.randint(0, 2)
        # Default mummy speed
        self.speed = 1 + random.randint(1, 3)
        # image for sprite of mummy
        self.image = constant.mummy_image_sprite
        # Get and set position of mummy
        self.rect = self.image.get_rect()
        self.rect.x = constant.default_mummy_posX + random.randint(0, 300)
        self.rect.y = constant.default_mummy_posY
        # Define random number
        self.random_nb = random.randint(0, 5)

    def damage(self, amount, player, knowback):
        self.health -= amount
        if self.health <= 0:
            player.score += self.kill_point
            self.game.check_score()
            self.rect.x = constant.default_mummy_posX
            self.rect.y = constant.default_mummy_posY
            self.health = self.max_health
            self.speed = random.randint(1, 3)
        else:
            self.rect.x = self.rect.x + knowback

    def update_health_bar(self, surface):
        # Definition of life bar color (rgb)
        bar_color = (111, 210, 46)
        background_bar_color = (0, 0, 0)
        # Definition of life bar position
        bar_position = [self.rect.x + 45, self.rect.y - 5 + self.random_nb, self.health, 5]
        background_bar_position = [self.rect.x + 45, self.rect.y - 5 + self.random_nb, self.max_health, 5]
        # Draw life bar
        pygame.draw.rect(surface, background_bar_color, background_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # Check not collision with player
        if not self.game.check_collision(self, self.game.all_players):
            # Forward monster
            self.rect.x -= self.speed
        elif self.game.check_collision(self, self.game.all_players):
            # Apply damage to player
            self.game.player.damage(self.attack)

