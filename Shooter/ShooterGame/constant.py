import pygame
import game
from player import Player

# This fil save all constants variables

# Screen variables
screen_width = 1080
screen_height = 720

# Game variables
game_name = "Shooter_Blanck"
background_default = pygame.image.load('assets/bg.jpg')
player_image_sprite = pygame.image.load('assets/player.png')
bullet_image_sprite = pygame.image.load('assets/projectile.png')
mummy_image_sprite = pygame.image.load('assets/mummy.png')

rotate_image_angle_bullet = 180
default_mummy_posX = 1000
default_mummy_posY = screen_height - (265 - (Player(game).rect.width/4))
