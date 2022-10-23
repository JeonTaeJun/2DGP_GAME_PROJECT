from pico2d import *
import my_ch
import main
import math



class ground:
    def __init__(self):
        self.x = 640
        self.y = 400
        self.image = load_image('MAP1.png')
        self.width = 1280
        self.hight = 1280

    def update(self):
        self.x -= main.player.dx
        self.y -= main.player.dy

        if (self.x < -1920):
            self.x += 3840
        if (self.x > 3200):
            self.x -= 3840
        if (self.y < -2160):
            self.y += 3840
        if (self.y > 2960):
            self.y -= 3840

    def draw(self):
            self.image.draw(self.x, self.y, self.width, self.hight)
