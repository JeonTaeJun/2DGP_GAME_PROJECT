from pico2d import *
import random
import os
import math


class skeleton :
    image = None
    def __init__(self):
        self.frame = 0
        self.direction =0
        self.x, self.y = random.randint(100, 1240) , random.randint(1024, 1124)
        self.dx =0
        self.dy =0
        self.HP = 20
        if skeleton.image == None:
            skeleton.image = load_image('skelton.png')
    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15

    def draw(self):
        self.image.clip_draw(self.frame*30,self.direction*56,30,56,self.x,self.y,50,60)
        draw_rectangle(*self.get_bb())

    def chase_update(self, player_x, player_y):
        self.dx, self.dy = ((player_x-self.x)/math.sqrt((player_x-self.x)** 2+(player_y-self.y) ** 2),
                          (player_y-self.y)/math.sqrt((player_x-self.x)** 2+(player_y-self.y) ** 2))

        self.x+=self.dx*2
        self.y+=self.dy*2
        if player_x > self.x:
            self.direction = 0
        elif player_x < self.y:
            self.direction = 1
        self.frame = (self.frame + 1) % 6
class zombie:
    image = None
    def __init__(self):
        self.frame = 0
        self.direction =0
        self.x, self.y = random.randint(1240, 1340) , random.randint(0, 1024)
        self.dx =0
        self.dy =0
        self.HP=30
        if zombie.image == None:
            zombie.image = load_image('zombie1.png')
    def draw(self):
        self.image.clip_draw(self.frame*31,self.direction*73,31,73,self.x,self.y,60,80)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return (self.x-15,self.y-20,self.x+15,self.y+20)
    def chase_update(self, player_x, player_y):
        self.dx, self.dy = ((player_x-self.x)/math.sqrt((player_x-self.x)** 2+(player_y-self.y) ** 2),
                          (player_y-self.y)/math.sqrt((player_x-self.x)** 2+(player_y-self.y) ** 2))

        self.x+=self.dx*2
        self.y+=self.dy*2
        if player_x > self.x:
            self.direction = 0
        elif player_x < self.x:
            self.direction = 1
        self.frame = (self.frame + 1) % 6