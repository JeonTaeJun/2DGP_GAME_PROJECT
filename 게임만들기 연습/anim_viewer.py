from pico2d import *

open_canvas()

character = load_image('mych.png')
arrow = load_image('arrow.png')
background = load_image('grass.png')
dog = load_image('cerberos-left.png')
def stop():
    frame = 0
    for x in range(0, 100, 10):
        clear_canvas()
        background.draw(400, 30)
        character.clip_draw(frame * 128, 1150, 128, 128, 750, 110)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.1)
        get_events()

def Draw_sword():
    frame = 0
    for x in range(750, 700, -10):
        clear_canvas()
        background.draw(400, 30)
        character.clip_draw(frame * 128, 1020, 128, 128, x, 110)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.1)
        get_events()

def attack(curx,finx):
    frame = 0
    for x in range(curx, finx, -5):
        clear_canvas()
        background.draw(400, 30)
        character.clip_draw(frame * 128, 890, 128, 128, x, 110)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.1)
        get_events()

def Move_draw_sword():
    frame = 0
    frame2 = 0
    xx=110
    for x in range(675, 515, -10):
        xx+=10
        clear_canvas()
        background.draw(400, 30)
        character.clip_draw(frame * 128, 250, 128, 128, x, 110)
        dog.clip_draw(frame2 * 97, 0, 97, 70, xx, 80)
        update_canvas()
        frame = (frame + 1) % 8
        frame2 = (frame2 + 1) % 5
        delay(0.1)
        get_events()
def sheathe():
    frame = 0
    for x in range(515, 475, -10):
        clear_canvas()
        background.draw(400, 30)
        character.clip_draw(frame * 128, 1020, 128, 128, x, 110)
        update_canvas()
        frame = (frame + 7) % 4
        delay(0.1)
        get_events()

def Move_sheathe_sword():
    frame = 0
    for x in range(475, 375, -10):
        clear_canvas()
        background.draw(400, 30)
        character.clip_draw(frame * 128, 128, 128, 128, x, 110)
        update_canvas()
        frame = (frame + 1) % 10
        delay(0.1)
        get_events()

def Guard():
    frame = 0
    for x in range(300,360,10):
        clear_canvas()
        background.draw(400, 30)
        character.clip_draw(9 * 128, 768, 128, 128, 375, 110)
        arrow.clip_draw(183,507,183,160,x,30)
        update_canvas()
        get_events()

def Die():
    frame = 0
    for x in range(375, 350, -5):
        clear_canvas()
        background.draw(400, 30)
        character.clip_draw(frame * 128, 768, 128, 128, x, 110)
        update_canvas()
        frame = (frame + 1) % 6
        delay(0.1)
        get_events()


while(True):
    stop()
    Draw_sword()
    delay(0.2)
    attack(700, 675)
    delay(0.2)
    Move_draw_sword()
    attack(515, 490)
    delay(0.2)
    sheathe()
    delay(0.2)
    Move_sheathe_sword()
    Guard()
    delay(0.3)
    Die()
    delay(0.5)