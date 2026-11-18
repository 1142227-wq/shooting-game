from pygame import *
from random import randint
# load functions for working with fonts separately
font.init()
game_font = font.Font(None, 36)

#background music
mixer.init()
mixer.music.load('back_music.ogg')
mixer.music.set_volume(1)
mixer.music.play()

destroy_effect = mixer.Sound('destroy_sound.ogg')

# Create the window
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

#Variable pictures:
img_back1 = transform.scale(image.load('map1.png'), (win_width, win_height + 50))
img_pistol = transform.scale(image.load("gun1.png"), (50, 70))
img_bazooka = transform.scale(image.load("gun2.png"), (50, 70))
img_minigun = transform.scale(image.load("gun3.png"), (50, 70))
img_bullet = transform.scale(image.load("bullet.png"), (15, 20))
img_zombie1 = transform.scale(image.load("zombie1.png"), (50, 50))
img_zombie2 = transform.scale(image.load("zombie2.png"), (50, 50))
img_zombie3 = transform.scale(image.load("zombie3.png"), (50, 50))


 
score = 0 
goal = 10 
lost = 0 
base_health = 10 
clock = time.Clock()
FPS = 60



# Enemy spawn settings
spawn_counter = 0
spawn_delay = randint(30, 60)
MAX_ENEMIES = 6 

# Zombie progression system
zombie_level = 1  # Current zombie level (1, 2, or 3)
zombies_killed = 0  # Track total zombies killed
ZOMBIES_PER_LEVEL = 10  # Zombies needed to advance to next level

class HealthBar:
    def __init__(self, x, y, width, height, max_health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = max_health
        self.current_health = max_health
        self.background_color = (128, 128, 128)  # Gray
        self.health_color = (255, 0, 0)  # Red

    def draw(self, surface):
        # Draw background (gray)
        draw.rect(surface, self.background_color, 
                 (self.x, self.y, self.width, self.height))
        # Draw current health (red)
        current_health_width = (self.current_health / self.max_health) * self.width
        draw.rect(surface, self.health_color,
                 (self.x, self.y, current_health_width, self.height))

    def decrease_health(self, amount=1):
        self.current_health = max(0, self.current_health - amount)
        return self.current_health <= 0

    def reset(self):
        self.current_health = self.max_health
        
    
class GameSprite(sprite.Sprite):# parent class
    def __init__(self, player_image, player_x, player_y, sice_x, sice_y, player_speed):
        sprite.Sprite.__init(set)# inherit all methods from the parent class
        self.image = player_image
        self.speed = player_speed
        self.rect = self.image.get_rect()#create rectangle around the sprite
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.y, self.rect.x))





class player(GameSprite):
    def __init__(self, player_image, player_x, player_y, sice_x, sice_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, sice_x, sice_y, player_speed)
        self.bullet_speed = -10
        self.reload_time = 30# 0.5s
        self.reload_counter = 0
        


    

