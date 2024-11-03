from monster import Monster

import player
import pygame


class Game:
    def __init__(self):
        self.is_playing = False
        self.player = player.Player(self)
        self.pressed = {}
        self.all_mummy = pygame.sprite.Group()

    def start_game(self):
        self.is_playing = True
        self.spawn_monster()

    def game_over(self):
        self.all_mummy = pygame.sprite.Group()
        self.player.all_bullet = pygame.sprite.Group()
        self.pressed = {}
        self.is_playing = False

    def update(self, screen):
        self.player_actions(screen)
        self.bullet_actions(screen)
        self.monster_actions(screen)

    def check_score(self):
        level = int(self.player.score / 100)

        if len(self.all_mummy) - 1 < ((level + 1) * 2):
            self.spawn_monster()

        if 15 <= self.player.score <= 16:
            self.spawn_monster()
            self.player.attack += 3
        elif 30 <= self.player.score <= 31:
            self.spawn_monster()
            self.player.attack += 2
        elif 50 <= self.player.score <= 51:
            self.spawn_monster()
            self.player.attack += 1
        elif self.player.score >= 150:
            self.spawn_monster()
            self.player.attack += 2

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_mummy.add(monster)

    def player_actions(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_LEFT):
            self.player.dont_move()
        elif (self.pressed.get(pygame.K_RIGHT) and self.player.rect.x +
              (self.player.rect.width - 20) < screen.get_width()):
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -20:
            self.player.move_left()

    def bullet_actions(self, screen):
        # Get all bullet and move it
        for bullets in self.player.all_bullet:
            bullets.move()

        self.player.all_bullet.draw(screen)

    def monster_actions(self, screen):
        for monster in self.all_mummy:
            monster.forward()
            monster.update_health_bar(screen)

        self.all_mummy.draw(screen)