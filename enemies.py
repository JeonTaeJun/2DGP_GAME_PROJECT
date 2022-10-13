from pico2d import *
import random
import os
import math


class skeleton :
    def __init__(self):
        self.image = load_image('skelton.png')
        self.frame = 0
        self.direction =0
        self.x, self.y = random.randint(100, 1280), random.randint(100, 1024)
        self.dx =0
        self.dy =0
    def draw(self):
        self.image.clip_draw(self.frame*30,self.direction*56,30,56,self.x,self.y,40,50)

    def chase_update(self, player_x, player_y):
        self.dx, self.dy = ((player_x-self.x)/math.sqrt((player_x-self.x)** 2+(player_y-self.y) ** 2),
                          (player_y-self.y)/math.sqrt((player_x-self.x)** 2+(player_y-self.y) ** 2))

        self.x+=self.dx*2
        self.y+=self.dy*2
        if player_x > self.x:
            self.direction = 0
        elif player_x < self.y:
            self.direction = 1
