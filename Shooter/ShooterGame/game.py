from monster import Monster

import player
import pygame


class Game:

    def __init__(self):
        # Define game status
        self.is_playing = False
        # Init group for player only
        self.all_players = pygame.sprite.Group()
        # Init sprite player for game
        self.player = player.Player(self)
        # Add player in payer group
        self.all_players.add(self.player)
        # Stock last key activated
        self.pressed = {}
        # Definition new group of monsters
        self.all_mummy = pygame.sprite.Group()
        # Variable fot last spawn
        self.last_spawn = 0

    def start_game(self):
        # Start game
        self.is_playing = True
        # Spawn monster
        self.spawn_monster()

    def game_over(self):
        self.all_mummy = pygame.sprite.Group()
        self.player.all_bullet = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.bar_color = self.player.default_bar_color
        self.player.rect = self.player.default_rect
        self.player.score = 0
        self.pressed = {}
        self.is_playing = False

    def update(self, screen):
        # Apply player sprite in game
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        # Apply monsters sprite in game
        self.all_mummy.draw(screen)

        # Get all bullet and move it
        for bullets in self.player.all_bullet:
            bullets.move()

        # Get all monsters sprite in game
        for monster in self.all_mummy:
            monster.forward()
            monster.update_health_bar(screen)

        # Apply bullet
        self.player.all_bullet.draw(screen)

        # Check player direction
        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_LEFT):
            self.player.nothing_move()
        elif self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + (
                self.player.rect.width - 20) < screen.get_width():
            self.player.move_right()
            lastDir = "Right"
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -20:
            lastDir = "Left"
            self.player.move_left()

    def check_score(self):
        if 15 <= self.player.score <= 16:
            self.spawn_monster()
            self.player.attack += 3
        elif 30 <= self.player.score <= 31:
            self.spawn_monster()
            self.player.attack += 2
        elif 50 <= self.player.score <= 51:
            self.spawn_monster()
            self.player.attack += 1
        elif self.player.score >= 150 and self.last_spawn == 0:
            self.spawn_monster()
            self.player.attack += 2
            self.last_spawn = 1

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        # Create monster
        monster = Monster(self)
        # Add new monster in group
        self.all_mummy.add(monster)
