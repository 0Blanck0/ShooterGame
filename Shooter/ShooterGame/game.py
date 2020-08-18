from monster import Monster

import player
import pygame


class Game:

    def __init__(self):
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
        # Spawn monster
        self.spawn_monster()
        # Variable fot last spawn
        self.last_spawn = 0

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
