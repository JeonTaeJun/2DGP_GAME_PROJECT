from pico2d import *
import Map
import my_ch
import enemies
import collide
import framework
import gameover
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
time = 0
time_s = 0
time_z = 0
skeltons = []
zombies =[]
MAPS=[]
player=None
MAP = None
at = None
at_list = []
num = 1
open_canvas()
def enter():
    mapset = [[-1280, 1280], [0, 1280], [1280, 1280], [-1280, 0], [0, 0], [1280, 0], [-1280, -1280], [0, -1280],
             [1280, -1280]]
    global skeltons
    global zombies
    global player
    global MAP
    global at_list
    global num
    global z_list_size
    global s_list_size
    global at
    global time
    global time_s
    global time_z
    global MAPS
    z_list_size = 0
    s_list_size = 0
    skeltons = [enemies.skeleton() for i in range(s_list_size)]
    zombies = [enemies.zombie() for i in range(z_list_size)]
    MAPS = [Map.ground()for i in range(9)]
    for i in range(9):
        MAPS[i].x=mapset[i][0]
        MAPS[i].y=mapset[i][1]
    player = my_ch.my_player()
    at_list = []
    time = 1.0
    time_s = 0.0
    time_z = 0.0

def exit():
    global skeltons
    global zombies
    global MAP
    global player

    del skeltons
    del zombies
    del MAP
    del player



def update():
    global time
    global time_s
    global time_z
    global num
    global at_list
    global at

    for i in range(9):
        MAPS[i].update()
    player.update()
    time += 0.1
    time_s += 0.05
    time_z += 0.05
    if time > 1.0:
        time = 0
        at = attack.basic_attack()
        at.player_x=player.player_x
        at.player_y=player.player_y
        if player.dir ==3:
            at.dir=-1
        elif player.dir ==2:
            at.dir = 1

        at_list.append(at)

    if time_s > 1.0:
        time_s=0
        skeltons.append(enemies.skeleton())
    if time_z > 1.0:
        time_z=0
        zombies.append(enemies.zombie())

    for at in at_list:
        at.update()
    for skelton in skeltons:
        skelton.chase_update(player.player_x, player.player_y)
    for zombie in zombies:
        zombie.chase_update(player.player_x, player.player_y)
    for zombie in zombies:
        if collide.collide_player(player,zombie)==True:
            player.HP-=1
    for skelton in skeltons:
        if collide.collide_player(player,skelton)==True:
            player.HP-=1

    for i in range(len(skeltons)):
        for j in range(len(zombies)):
            if collide.collide_player(skeltons[i], zombies[j]) == True:
                skeltons[i].x-=skeltons[i].dx*2


    ds_list=[]
    da_list=[]
    for i in range(len(skeltons)):
        for j in range(len(at_list)):
            s=skeltons[i]
            a=at_list[j]
            if collide.collide_player(s,a) == True:
                da_list.append(j)
                skeltons[i].HP -= 10
                if skeltons[i].HP <= 0:
                    ds_list.append(i)
    da_list = list(set(da_list))
    ds_list = list(set(ds_list))
    for da in da_list:
        del at_list[da]
    for ds in ds_list:
        del skeltons[ds]

    da_list = []
    dz_list = []

    for i in range(len(zombies)):
        for j in range(len(at_list)):
            z = zombies[i]
            a = at_list[j]
            if collide.collide_player(z, a) == True:
                da_list.append(j)
                zombies[i].HP -= 10
                if zombies[i].HP <= 0:
                    dz_list.append(i)

    da_list = list(set(da_list))
    dz_list = list(set(dz_list))

    for da in da_list:
        del at_list[da]
    for dz in dz_list:
        del zombies[dz]


    print(player.HP)
    if player.HP < 0:
        framework.change_state(gameover)

def draw():
    global time
    global num
    global at
    clear_canvas()
    for i in range(9):
        MAPS[i].draw()
    player.draw()
    for at in at_list:
        at.draw()
    for skelton in skeltons:
        skelton.draw()
    for zombie in zombies:
        zombie.draw()

    update_canvas()
def pause():
    pass

def resume():
    pass
