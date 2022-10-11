from pico2d import *

up_down_dir=0

def handle_events(handle):
    global running
    global up_down_dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
           if event.key == SDLK_LEFT:
                handle.move_x -= 1
                handle.direction = 3
                up_down_dir = 1
           elif event.key == SDLK_RIGHT:
               handle.move_x += 1
               handle.direction = 2
               up_down_dir = 2
           elif event.key == SDLK_UP:
               handle.move_y += 1
               if up_down_dir == 1:
                   handle.direction = 3
               elif up_down_dir ==2:
                    handle.direction = 2
           elif event.key == SDLK_DOWN:
               handle.move_y -= 1
               if up_down_dir == 1:
                   handle.direction = 3
               elif up_down_dir ==2:
                    handle.direction = 2
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                handle.move_y -= 1
                if up_down_dir ==1:
                    handle.direction = 1
                else:
                    handle.direction = 0
            elif event.key == SDLK_DOWN:
                handle.move_y += 1
                if up_down_dir == 1:
                    handle.direction = 1
                else:
                    handle.direction = 0
            elif event.key == SDLK_LEFT:
                handle.move_x += 1
                handle.direction = 1
            elif event.key == SDLK_RIGHT:
                handle.move_x -= 1
                handle.direction = 0