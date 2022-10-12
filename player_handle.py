from pico2d import *

running =True
direction=0
up_down_dir = 0
move_x = 0
move_y = 0
def player_handle():
    global running
    global direction
    global up_down_dir
    global move_x
    global move_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                move_x -= 1
                direction = 3
                up_down_dir = 1
            elif event.key == SDLK_RIGHT:
                move_x += 1
                direction = 2
                up_down_dir = 2
            elif event.key == SDLK_UP:
                move_y += 1
                if up_down_dir == 1:
                    direction = 3
                elif up_down_dir == 2:
                    direction = 2
            elif event.key == SDLK_DOWN:
                move_y -= 1
                if up_down_dir == 1:
                    direction = 3
                elif up_down_dir == 2:
                    direction = 2
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                move_y -= 1
                if up_down_dir == 1:
                    direction = 1
                else:
                    direction = 0
            elif event.key == SDLK_DOWN:
                move_y += 1
                if up_down_dir == 1:
                    direction = 1
                else:
                    direction = 0
            elif event.key == SDLK_LEFT:
                move_x += 1
                direction = 1
            elif event.key == SDLK_RIGHT:
                move_x -= 1
                direction = 0