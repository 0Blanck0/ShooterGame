import pygame
import constant

# Player class (all function for all player)

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        # Basic and max health point
        self.health = 100
        self.max_health = 100
        # Basic attack point
        self.attack = 10
        # Basic player speed
        self.speed = 8
        # Default player score
        self.score = 0
        # Bullet def
        self.all_bullet = pygame.sprite.Group()
        # Image for player sprite
        self.image = constant.player_image_sprite
        self.rect = self.image.get_rect()
        # Set default position on screen
        self.rect.x = (constant.screen_width/2) - self.rect.width/2
        self.rect.y = constant.screen_height - (265 - (self.rect.width/4))

    def update_health_bar(self, surface):
        # Definition of life bar color (rgb)
        bar_color = (111,210,46)
        background_bar_color = (0,0,0)
        # Definition of life bar position
        bar_position = [self.rect.x+45, self.rect.y-5, self.health, 5]
        background_bar_position = [self.rect.x+45, self.rect.y-5, self.max_health, 5]
        # Draw life bar
        pygame.draw.rect(surface, background_bar_color, background_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def fire(self, direction):
        # Create new bullet in the game
        bullet = Bullet(self, direction)
        if direction == "Left":
            bullet.rotate()
        # Add new bullet in bullet group
        self.all_bullet.add(bullet)

    def nothing_move(self):
        # Don't move player
        self.rect.x = self.rect.x

    def move_right(self):
        # Check mummy collision
        if not self.game.check_collision(self, self.game.all_mummy):
            # Move player in right
            self.rect.x += self.speed

    def move_left(self):
        # Move player in left
        self.rect.x -= self.speed


class Bullet(pygame.sprite.Sprite):

    def __init__(self, player, direction):
        super().__init__()
        # Add player in attribute
        self.player = player
        # speed of bullet
        if direction == "Right":
            self.speed = 12
        elif direction == "Left":
            self.speed = -12
        # Definition default angle of image
        self.angle = 0
        # Bullet image for sprite
        self.image = constant.bullet_image_sprite
        # Get and set size of bullet
        self.rect = self.image.get_rect()
        self.width = int(self.rect.width/10)
        self.height = int(self.rect.height/10)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # Set bullet position
        self.rect.x = player.rect.x + (player.rect.width/3)
        self.rect.y = player.rect.y + (player.rect.width/3)
        # Save image of sprite
        self.origin_image = self.image

    def remove(self):
        # Remove actual select bullet
        self.player.all_bullet.remove(self)

    def rotate(self):
        # Rotate object function
        self.angle = constant.rotate_image_angle_bullet
        self.image = pygame.transform.rotate(self.origin_image, self.angle)

    def move(self):
        # Move bullet
        self.rect.x += self.speed
        # It's outside the screen destroy it
        if self.rect.x > constant.screen_width or self.rect.x < -50:
            self.remove()
        # If bullet enter in collision with monster remove self
        for monster in self.player.game.check_collision(self, self.player.game.all_mummy):
            self.remove()
            monster.damage(self.player.attack, self.player)
            