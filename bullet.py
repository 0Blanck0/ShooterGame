import constant
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        self.player = player
        self.speed = constant.default_bullet_speed
        self.image = constant.bullet_image_sprite #Bullet image for sprite
        #Set bullet size
        self.rect = self.image.get_rect()
        self.width = int(self.rect.width / 10)
        self.height = int(self.rect.height / 10)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # Set bullet position
        self.rect.x = player.rect.x + (player.rect.width / 3)
        self.rect.y = player.rect.y + (player.rect.width / 3)
        # Save image of sprite
        self.origin_image = self.image
        # Define Knockback
        self.knockback = 20

    def remove(self):
        self.player.all_bullet.remove(self)

    def move(self):
        self.rect.x += self.speed
        # It's outside the screen destroy it
        if self.rect.x > constant.screen_width or self.rect.x < -50:
            self.remove()
        # If bullet enter in collision with monster remove self
        for monster in self.player.game.check_collision(self, self.player.game.all_mummy):
            self.remove()
            monster.damage(self.player.attack, self.player, self.knockback)
