from pico2d import *

class basic_attack:
    def __init__(self):
        self.attack=load_image('at.png')
        self.ax=0
        self.power=10
        self.player_x=0
        self.player_y=0

    def get_bb(self):
        return self.player_x + self.ax - 4, self.player_y - 4, self.player_x+ self.ax + 4, self.player_y + 4

    def draw(self,player_x,player_y,direction):
        self.player_x=player_x
        self.player_y=player_y
        self.attack.draw(player_x + self.ax, player_y, 10, 10)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.ax += 20

