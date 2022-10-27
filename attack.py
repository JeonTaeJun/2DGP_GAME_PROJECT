from pico2d import *

class basic_attack:
    def __init__(self):
        self.attack=load_image('nomal_at.png')
        self.ax=0
        self.power=10
        self.x=640
        self.y=512
        self.dx=0
        self.dy=0
        self.dir=0
        self.speed=25

    def get_bb(self):
        return self.x + self.dir*self.ax - 4, self.y - 4, self.x + self.dir*self.ax + 4, self.y + 4
    def draw(self):
        self.attack.clip_draw(0,self.dir*30,170,30,self.x +100+ self.dir, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        pass
