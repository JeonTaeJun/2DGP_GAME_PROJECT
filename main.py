from pico2d import *
import Map
import my_ch
import enemies
import framework
import gameover
import game_world
import collide
import attack
def handle_events():

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
#skeltons = []
#zombies =[]


player = None
MAP = None
skeleton = None
zombie = None
#at = None
open_canvas()
def enter():
    maplist = [[-1280, 1024], [0, 1024], [1280, 1024], [-1280, 0], [0, 0], [1280, 0], [-1280, -1024], [0, -1024],
             [1280, -1024]]
    #global skeltons
    #global zombies
    global player
    global MAP
    #global z_list_size
    #global s_list_size
    global time_s
    global time_z
    global MAPS
    global skeleton
    global zombie
    #skeltons = [enemies.skeleton() for i in range(s_list_size)]
    #zombies = [enemies.zombie() for i in range(z_list_size)]
    if zombie == None:
        zombie = enemies.zombie()
    if skeleton == None:
        skeleton = enemies.skeleton()
    if player == None:
        player = my_ch.my_player()

    MAPS = [Map.ground() for i in range(0,9)]
    for i in range(9):
        MAPS[i].x=maplist[i][0]
        MAPS[i].y=maplist[i][1]
    for i in range(9):
        game_world.add_object(MAPS[i],0)

    game_world.add_object(player, 1)
    game_world.add_object(zombie, 2)
    game_world.add_object(skeleton, 3)
    time_s = 0.0
    time_z = 0.0

def exit():
    global skeleton
    global zombie
    global MAP
    global player

    del skeleton
    del zombie
    del MAP
    del player



def update():
    global time_s
    global time_z
    global player
    global zombie
    global skeleton

    #for i in range(9):
     #   MAPS[i].update()
    #player.update()

    time_s += 0.1
    time_z += 0.1

    #if time_s >= 1:
     #   game_world.add_object(skeleton,3)
        #time_s=0
        #skeltons.append(enemies.skeleton())
    #if time_z >= 1:
     #   game_world.add_object(zombie, 2)
        #time_z=0
        #zombies.append(enemies.zombie())

    for game_Object in game_world.all_objects():
        game_Object.update()

    print(time_s)

   # for skelton in skeleton:
    #    skelton.chase_update(player.player_x, player.player_y)
    #for zombie in zombie:
     #   zombie.chase_update(player.player_x, player.player_y)
   # for zombie_ in zombie:
    #    if collide.collide_player(player,zombie_)==True:
     #       player.HP-=1
    #for skelton_ in skeleton:
     #   if collide.collide_player(player,skelton_)==True:
      #      player.HP-=1


    #print(player.HP)
    #if player.HP < 0:
     #   framework.change_state(gameover)


def draw():
    clear_canvas()
    for game_Object in game_world.all_objects():
        game_Object.draw()

    #for i in range(9):
     #   MAPS[i].draw()
   # player.draw()
    #for skelton in skeltons:
     #   skelton.draw()
    #for zombie in zombies:
     #   zombie.draw()

    update_canvas()
def pause():
    pass

def resume():
    pass
