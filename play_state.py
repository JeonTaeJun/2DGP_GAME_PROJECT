from pico2d import *
import Map
import my_ch
import enemies
import framework
import gameover
import game_world
import collide
import attack
def handle_events(): # dir=3 왼쪽 dir =4 오른쪽

    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                framework.quit()
            elif event.key == SDLK_LEFT:
                player.dx = -10
                player.dir = 3
            elif event.key == SDLK_RIGHT:
                player.dx = 10
                player.dir = 2
            elif event.key == SDLK_UP:
                player.dy = 10
            elif event.key == SDLK_DOWN:
                player.dy = -10
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                player.dy = 0
            elif event.key == SDLK_DOWN:
                player.dy = 0

            elif event.key == SDLK_LEFT:
                player.dx = 0
                player.dir=3
            elif event.key == SDLK_RIGHT:
                player.dx = 0
                player.dir=2

time_s = 0
time_z = 0

player = None
MAP = None
skeleton = None
zombie = None
at =None
skeleton_many = None
#at = None
open_canvas()
def enter():
    maplist = [[-1280, 1024], [0, 1024], [1280, 1024], [-1280, 0], [0, 0], [1280, 0], [-1280, -1024], [0, -1024],
             [1280, -1024]]
    global player
    global MAP
    global z_list_size
    global time_s
    global time_z
    global MAPS
    global at
    global skeleton_many
    if player == None:
        player = my_ch.my_player()

    MAPS = [Map.ground() for i in range(0,9)]
    for i in range(9):
        MAPS[i].x = maplist[i][0]
        MAPS[i].y = maplist[i][1]
    for i in range(9):
        game_world.add_object(MAPS[i],0)
    game_world.add_object(player,2)
    game_world.add_object(attack.circle_attack(),1)
    game_world.add_object(enemies.zombie(), 3)
    game_world.add_object(enemies.skeleton(), 3)
    time_s = 0.0
    time_z = 0.0

def exit():
    game_world.clear()

time_a=0
time_m_s =0
def update():
    global time_s
    global time_z
    global time_a
    global time_m_s
    global skeleton_many
    global zombies
    global skeleton
    time_s += 0.02
    time_z += 0.02
    time_a += 0.05
    time_m_s += 0.01

    if time_m_s >= 5:
        skeleton_many = [enemies.skeleton_many() for i in range(50)]
        time_m_s=0
        game_world.add_objects(skeleton_many, 3)

    if time_a>=1:
        time_a=0
        game_world.add_object(attack.basic_attack(), 1)

    if time_s >= 1:
        time_s=0
        game_world.add_object(enemies.skeleton(), 3)
    if time_z >= 1:
        game_world.add_object(enemies.zombie(), 3)
        time_z = 0

    for game_Object in game_world.all_objects():
        game_Object.update()

def draw():
    clear_canvas()
    for game_Object in game_world.all_objects():
        game_Object.draw()

    update_canvas()
def pause():
    pass

def resume():
    pass
