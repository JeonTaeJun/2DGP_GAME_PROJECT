from pico2d import *
import random
import os
os.chdir('C:\\gameproject\\2DGP_GAME_PROJECT')

class skeleton :
    def __init__(self):
        self.image = load_image('skelton.png')
        self.frame = 0
        self.direction =0
        self.t=0.0
        self.x, self.y = random.randint(100, 1280), random.randint(100, 1024)
        self.sx, self.sy = self.x, self.y

    def draw(self):
        self.image.clip_draw(self.frame*30,self.direction*56,30,56,self.x,self.y,50,50)

    def update(self, player_x, player_y):
        self.t += 0.005
        self.x = (1 - self.t) * self.sx + self.t * player_x
        self.y = (1 - self.t) * self.sy + self.t * player_y