from pico2d import *
import player_handle
import os


class my_player:
    def __init__(self):
        self.character = load_image('characters_.png')
        self.player_x = 1280 // 2
        self.player_y = 1024 // 2
        self.frame = 0

    def draw(self):
        player_handle.player_handle()
        if player_handle.direction == 1:
            self.character.clip_draw(0, player_handle.direction * 35, 27, 35, self.player_x, self.player_y, 40, 40)

        elif player_handle.direction == 0:
            self.character.clip_draw(0, player_handle.direction * 35, 27, 35, self.player_x, self.player_y, 40, 40)

        elif player_handle.direction == 3:
            self.character.clip_draw(self.frame * 28, player_handle.direction * 35, 27, 35, self.player_x, self.player_y, 40, 40)

        elif player_handle.direction == 2:
            self.character.clip_draw(self.frame * 28, player_handle.direction * 35, 27, 35, self.player_x, self.player_y, 40, 40)

    def update(self):
        self.frame = (self.frame + 1) % 7

        if self.player_x < 0:
            self.player_x += 15
        elif self.player_x > 1280:
            self.player_x -= 15

        if self.player_y < 0:
            self.player_y += 15
        elif self.player_y > 1000:
            self.player_y -= 15

        self.player_x += player_handle.move_x * 10
        self.player_y += player_handle.move_y * 10