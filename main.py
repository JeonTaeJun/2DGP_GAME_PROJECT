from pico2d import *
import Map
import my_ch
import enemies
import collide
import framework
import title
import attack
direction=0
up_down_dir = 0
move_x = 0
move_y = 0
def handle_events():
    global direction
    global up_down_dir
    global move_x
    global move_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                framework.quit()
            elif event.key == SDLK_LEFT:
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

skeltons = []
zombies =[]
at = []
num=1
z_list_size=0
s_list_size=0
open_canvas()
def enter():
    global skeltons
    global zombies
    global player
    global MAP
    global at
    global num
    global z_list_size
    global s_list_size
    global ax
    global ay
    skeltons = [enemies.skeleton() for i in range(s_list_size)]
    zombies = [enemies.zombie() for i in range(z_list_size)]
    MAP = Map.ground()
    player = my_ch.my_player()
    at = [attack.basic_attack() for i in range (num)]
    ax = [player.player_x, ]
    ay = [player.player_y, ]
def exit():
    global skeltons
    global zombies
    global MAP
    global player

    del skeltons
    del zombies
    del MAP
    del player


time=0.0
time_s=0.0
time_z=0.0
def update():
    global time
    global time_s
    global time_z
    global num

    global z_list_size
    global s_list_size
    time += 0.05
    time_s +=0.05
    time_z +=0.05
    if time > 1.5:
        time = 0
        ax.append(player.player_x)
        ay.append(player.player_y)
        num += 1
        at.append(attack.basic_attack())
    if time_s > 1.0:
        time_s=0
        s_list_size+=1
        skeltons.append(enemies.skeleton())
    if time_z > 1.0:
        time_z=0
        z_list_size+=1
        zombies.append(enemies.zombie())

    player.update(move_x,move_y)

    for ats in at:
        ats.update()
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
    for i in range(len(skeltons)):
        for j in range(len(at)):
            s=skeltons[i]
            a=at[j]
            if collide.collide_player(s,a) == True:
                del at[j]
                skeltons[i].HP -= 10
                if skeltons[i].HP <= 0:
                    ds_list.append(i)

    for ds in ds_list:
        del skeltons[ds]

    dz_list = []

    for i in range(len(zombies)):
        for j in range(len(at)):
            z = zombies[i]
            a = at[j]
            if collide.collide_player(z, a) == True:
                del at[j]
                zombies[i].HP -= 10
                if zombies[i].HP <= 0:
                    dz_list.append(i)

    for dz in dz_list:
        del zombies[dz]


    print(player.HP)
    if player.HP < 0:
        framework.change_state(title)

def draw():
    global time
    global num
    MAP.draw()
    player.draw(direction,move_x,move_y)
    for ats in at:
        ats.draw(ax[num-1],ay[num-1],direction)
    for skelton in skeltons:
        skelton.draw()
    for zombie in zombies:
        zombie.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass
