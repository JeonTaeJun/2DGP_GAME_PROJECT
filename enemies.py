from pico2d import *
import random
import os
import math
import collide
import game_world
import play_state
import Map


deg=None
def random_deg():
    global deg
    deg = random.randint(0,360)
    return deg
class skeleton_many :
    image = None
    def __init__(self):
        self.frame = 0
        self.direction =0
        self.x, self.y = random.randint(play_state.player.player_x-300,play_state.player.player_x+300) ,\
                         random.randint(-200,0)
        self.dx = 0
        self.dy = 0
        self.speed = 15
        self.HP = 20
        self.power = 5
        if skeleton_many.image == None:
            skeleton_many.image = load_image('skelton.png')
    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15

    def draw(self):
        self.image.clip_draw(self.frame*30,self.direction*56,30,56,self.x,self.y,50,60)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.speed
        self.x -= play_state.player.dx
        self.y -= play_state.player.dy
        if 640 > self.x:
            self.direction = 0
        elif 640 < self.x:
            self.direction = 1
        self.frame = (self.frame + 1) % 6

        if self.HP<0:
            game_world.remove_object(self)

class skeleton :
    image = None
    def __init__(self):
        self.deg = random_deg()
        self.frame = 0
        self.direction =0
        self.x, self.y = play_state.player.player_x+(math.cos(math.radians(self.deg))*800),\
                         play_state.player.player_y+(math.sin(math.radians(self.deg))*800)
        self.dx = 0
        self.dy = 0
        self.HP = 20
        self.power = 5
        if skeleton.image == None:
            skeleton.image = load_image('skelton.png')
    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15

    def draw(self):
        self.image.clip_draw(self.frame*30,self.direction*56, 30, 56, self.x, self.y, 50, 60)
        draw_rectangle(*self.get_bb())

    def update(self):#, player_x, player_y):
        self.dx, self.dy = (( play_state.player.player_x - self.x) / math.sqrt((play_state.player.player_x - self.x) ** 2 + (play_state.player.player_y - self.y) ** 2),
                            (play_state.player.player_y - self.y) / math.sqrt((play_state.player.player_x - self.x) ** 2 + (play_state.player.player_y - self.y) ** 2))

        self.x += self.dx * 2
        self.y += self.dy * 2
        self.x -= play_state.player.dx
        self.y -= play_state.player.dy
        if 640 > self.x:
            self.direction = 0
        elif 640 < self.x:
            self.direction = 1
        self.frame = (self.frame + 1) % 6

        if self.HP<0:
            game_world.remove_object(self)
class zombie:
    image = None
    def __init__(self):
        self.deg = random_deg()
        self.frame = 0
        self.direction = 0
        self.x, self.y = play_state.player.player_x+(math.cos(math.radians(self.deg))*800),\
                         play_state.player.player_y+(math.sin(math.radians(self.deg))*800)
        self.dx = 0
        self.dy =0
        self.HP= 30
        self.power = 10
        if zombie.image == None:
            zombie.image = load_image('zombie1.png')
    def draw(self):
        self.image.clip_draw(self.frame*31,self.direction*73,31,73,self.x,self.y,60,80)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return (self.x-15,self.y-20,self.x+15,self.y+20)
    def update(self):#, player_x, player_y):
        self.dx, self.dy = ((play_state.player.player_x-self.x)/math.sqrt((play_state.player.player_x-self.x)** 2+(play_state.player.player_y-self.y) ** 2),
                          (play_state.player.player_y-self.y)/math.sqrt((play_state.player.player_x-self.x)** 2+(play_state.player.player_y-self.y) ** 2))

        self.x += self.dx*2
        self.y += self.dy*2
        self.x -= play_state.player.dx
        self.y -= play_state.player.dy
        if 640 > self.x:
            self.direction = 0
        elif 640 < self.x:
            self.direction = 1
        self.frame = (self.frame + 1) % 6

        if self.HP<0:
            game_world.remove_object(self)
