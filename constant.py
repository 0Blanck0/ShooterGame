import pygame
import game
from player import Player

# This fil save all constants variables

# Color
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)

# Screen variables
screen_width = 1080
screen_height = 720

# Game variables
game_name = "MyShooterGame by Alexandre ELISABETH"
background_default = pygame.image.load('assets/bg.jpg')
banner_default = pygame.image.load('assets/banner.png')
player_image_sprite = pygame.image.load('assets/player.png')
bullet_image_sprite = pygame.image.load('assets/projectile.png')
mummy_image_sprite = pygame.image.load('assets/mummy.png')

# Player variables
default_player_health = 100
default_player_attack = 10
default_player_speed = 1

# Bullet variables
default_bullet_speed = 2

# Mobs variables
# - Mummy
default_mummy_posX = 1000
default_mummy_posY = screen_height - (265 - (Player(game).rect.width / 4))
default_mummy_health = 100
default_mummy_attack = 0.1
default_mummy_speed = 0.5
default_mummy_bar_color = (111, 210, 46)
default_mummy_bar_empty_color = (0, 0, 0)
