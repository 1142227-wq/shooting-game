from pygame import *

#step 1 prepare music

mixer.init()
mixer.music.load('back_music.ogg')
mixer.music.set_volume(1)
mixer.music.play()

destroy_effect = mixer.Sound('destroy_sound.ogg')

#step two create the widow
win_widht = 700
win_heght = 500
display.set_caption('stooter')
window = display.set_mode((win_widht, win_heght))

#step 3 prepare images
img_back = transform.scale(image.load('map1.png'), (win_widht, win_heght))
img_pisto1 = transform.scale(image.load('gun1.png'), (50, 70))
img_bazooka = transform.scale(image.load('gun2.png'), (50, 70))
img_minigun = transform.scale(image.load('gun3.png'), (50, 70))
img_bullet = transform.scale(image.load('bullet.png'), (50, 20))
img_zombie = transform.scale(image.load('zombie1.png'), (50, 50))
img_zombie2 = transform.scale(image.load('zombie2.png'), (50, 50))
img_zombie3 = transform.scale(image.load('zombie3.png'), (50, 50))

#step 4 create class
class HealthBar:
    def __init__(self, x, y, height, max_health):
        self,x = x
        self,y = y
        self,width = width
        self,height = height
        self,max_health=max_health
        self.current_health = max_health
        self.background_color = (128, 128, 128)#gray
        self.health_color = (255, 0, 0)#red

    def draw(self, surface):#Window
        draw.rect(surface, self.background_color, (self.x, self.y, self.width, self.height))#gray
        current_health_width = (self.current_health / self.max_health)*self.width

        draw.rect(surface, self.health_color, (self.x, self.y, current_health_width, self.height))#red
    
    def decrease_health(self, amount):
        self.current_health = max(0, self.current_health - amount)# make sure health doesn't go below 0
       return self.current_health == 0


    def reset_game():
        self.current_health = self.max_health
score = 0
goal = 10
loat = 0
base_health = 10
 
def draw_gui():
    score_text = game_font.render("Score" + str(score))








run = True
clock = time.Clock()
FPS = 60
while run:
    display.update()
    clock.tick(FPS)

