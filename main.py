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
img_back = treansfrom.scale(image.load('map1.png'), (win_widht, win_heght))
img_pisto1 = treansfrom.scale(image.load('gun1.png'), (50, 70))
img_bazooka = treansfrom.scale(image.load('gun2.png'), (50, 70))
img_minigun = treansfrom.scale(image.load('gun3.png'), (50, 70))
img_bullet = treansfrom.scale(image.load('bullet.png'), (50, 20))
img_zombie = treansfrom.scale(image.load('zombie1.png'), (50, 50))
img_zombie2 = treansfrom.scale(image.load('zombie2.png'), (50, 50))
img_zombie3 = treansfrom.scale(image.load('zombie3.png'), (50, 50))

#step 4 create class
class HealthBar:
    def__init__(self, x, y, height, max_health):
        self,x = x
        self,y = y
        self,width = width
        self,height = height
        self,max_health=max_health
        self.current_health = max_health
        self.background_color = (128, 128, 128)#gray
        self.health_color = (255, 0, 0)#red

    def.draw(self, surface):#Window
        draw.rect(surface, self,background_color, (self.x, self.y, self.width, self.height))#gray
        
    


