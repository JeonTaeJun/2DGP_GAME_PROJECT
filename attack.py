from pico2d import *
import my_ch
class basic_attack:
    def __init__(self):
        self.attack=load_image('at.png')
        self.ax=0
        self.power=10
        self.player_x=0
        self.player_y=0
        self.dir=0
        self.speed=25

    def get_bb(self):
        return self.player_x + self.dir*self.ax - 4, self.player_y - 4, self.player_x + self.dir*self.ax + 4, self.player_y + 4
    def draw(self):
        self.attack.draw(self.player_x + self.dir*self.ax, self.player_y, 20, 20)
        draw_rectangle(*self.get_bb())


    def update(self):
        self.ax += self.speed

