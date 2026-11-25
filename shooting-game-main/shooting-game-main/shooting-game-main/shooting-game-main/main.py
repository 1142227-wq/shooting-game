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
        self.current_weapon ="pistol"
        self.weapon_demage = 1

    def update(self):
        keys = key.get_pressed()# which key are pressed

        if keys[K_A] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_d] and self.rect.x <win_width - 50:
            self.rect.x += self.speed

        if keys[K_w] and self.rect.y > 75:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.x < win_width - 70:
            self.rect.y += self.speed

        if keys[k_1]:
            self.image = img_pistol#Update image
            self.shift_x = 8
            self.shift_y = -5
            self.bullet_speed = -10
            self.reload_time = 30# 0.5s  
            self.current_weapon ="pistol"
            self.weapon_demage = 1#pistol demage

        if keys[k_2]:
            self.image = img_bazooka#Update image
            self.shift_x = -22
            self.shift_y = -15
            self.bullet_speed = -8
            self.reload_time = 60# 0.5s  
            self.current_weapon ="bazooka"
            self.weapon_demage = 3#pistol demage      


        if keys[k_3]:
            self.image = img_minigun#Update image
            self.shift_x = -13
            self.shift_y = -11
            self.bullet_speed = -12
            self.reload_time = 15# 0.5s  
            self.current_weapon ="minigun"
            self.weapon_demage = 2#pistol demage      

        if self.reload_counter > 0:
            self.reload_counter -= 1

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, sice_x, sice_y, player_speed, zombie_type=1):
        super().__init__(player_image, player_x, player_y, sice_x, sice_y, player_speed)
        self.zombie_type = zombie_type
        self.health = zombie_level
    def update(self):
        self.rect.y += self.speed

        if self.rect.y > win_height:#when they go over the screen, respawn
            self.rect.x = randint(40, win_width - 50)
            self.rect.y = 0 #take the enemy back to the top

