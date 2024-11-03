import pygame
import constant
import random


class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.health = constant.default_mummy_health
        self.attack = constant.default_mummy_attack
        self.kill_point = 2 + random.randint(0, 2)
        self.speed = constant.default_mummy_speed + random.uniform(0.1, 0.3)
        self.image = constant.mummy_image_sprite
        self.rect = self.image.get_rect()
        self.rect.x = constant.default_mummy_posX + random.randint(0, 300)
        self.rect.y = constant.default_mummy_posY
        self.random_nb = random.randint(0, 5)

    def damage(self, amount, player, knockback):
        self.health -= amount

        if self.health <= 0:
            player.score += self.kill_point

            self.game.check_score()
            self.destroy()
        else:
            self.rect.x = self.rect.x + knockback

    def update_health_bar(self, surface):
        bar_color = constant.default_mummy_bar_color
        background_bar_color = constant.default_mummy_bar_empty_color

        bar_position = [self.rect.x + 45, self.rect.y - 5 + self.random_nb, self.health, 5]
        background_bar_position = [self.rect.x + 45, self.rect.y - 5 + self.random_nb, constant.default_mummy_health, 5]

        pygame.draw.rect(surface, background_bar_color, background_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        tmp_grp =  pygame.sprite.Group()
        tmp_grp.add(self.game.player)

        if not self.game.check_collision(self, tmp_grp):
            self.rect.x -= self.speed
        elif self.game.check_collision(self, tmp_grp):
            self.game.player.damage(self.attack)

    def destroy(self):
        self.game.all_mummy.remove(self)
