
from pico2d import *
from handle import *
import enemies
import os


os.chdir('C:\\gameproject\\2DGP_GAME_PROJECT')

class handle:
    move_x=0
    move_y=0
    direction =0 # 3-왼쪽 2-오른쪽 1-왼쪽 아이들 0-오른쪽아이들

running = True
player_x = 1280 // 2
player_y = 1024 // 2
frame = 0
frame2 = 0

open_canvas()
ground = load_image('MAP1.png')
character_left = load_image('characters_left.png')
character_right = load_image('characters_right.png')
character_right_idle = load_image('characters_idle_R.png')
character_left_idle = load_image('characters_idle_L.png')
character = load_image('characters_.png')
pico2d.resize_canvas(1280, 1024)
skeltons = [enemies.skeleton() for i in range(11)]

while running:
    clear_canvas()
    ground.draw(640, 550, 1280, 1024)
    if handle.direction == 1:
        character.clip_draw(frame * 28, handle.direction*35, 27, 35, player_x, player_y, 50, 50)

    elif handle.direction == 0:
        character.clip_draw(frame * 28, handle.direction*35, 27, 35, player_x, player_y, 50, 50)

    elif handle.direction == 3:
        character.clip_draw(frame * 28, handle.direction*35, 27, 35, player_x, player_y, 50, 50)

    elif handle.direction == 2:
        character.clip_draw(frame * 28, handle.direction*35, 27, 35, player_x, player_y, 50, 50)

    for skelton in skeltons:
        skelton.update(player_x,player_y)

    for skelton in skeltons:
        if player_x > skelton.sx:
            skelton.direction=0
            skelton.draw()
        elif player_x < skelton.sx:
            skelton.direction = 1
            skelton.draw()

    update_canvas()
    handle_events(handle)
    frame = (frame + 1) % 7
    frame = (frame + 1) % 3
    if player_x < 0:
        player_x += 15
    elif player_x > 1280:
        player_x -= 15

    if player_y < 0:
        player_y += 15
    elif player_y > 1000:
        player_y -= 15

    for skelton in skeltons:
        skelton.frame=(skelton.frame + 1) % 6
    player_x += handle.move_x * 15
    player_y += handle.move_y * 15
    delay(0.05)

close_canvas()