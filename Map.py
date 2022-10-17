from pico2d import *

class ground:
    def __init__(self):
        self.image = load_image('MAP1.png')
    def draw(self):
        self.image.draw(640, 550, 1280, 1024)
