import random

from pico2d import *
import play_state
import collide
import game_world
class basic_attack:
    def __init__(self):
        self.attack=load_image('basicat.png')
        self.ax=0
        self.power=10
        self.x=640
        self.y=512
        self.dir=0
        self.mon = random.randint(0,len(game_world.objects[3])-1)
        self.dx, self.dy = \
            ((game_world.objects[3][self.mon].x - self.x) / math.sqrt((game_world.objects[3][self.mon].x - self.x) ** 2 + (game_world.objects[3][self.mon].y - self.y) ** 2),
            (game_world.objects[3][self.mon].y - self.y) / math.sqrt((game_world.objects[3][self.mon].x - self.x) ** 2 + (game_world.objects[3][self.mon].y - self.y) ** 2))

        if play_state.player.dir == 3:
            self.speed = -25
        elif play_state.player.dir == 2:
            self.speed = 25
        else:
            self.speed = 25

    def get_bb(self):

        return self.x - 4, self.y - 4, self.x + 4, self.y + 4
    def draw(self):

        self.attack.clip_draw(0, 0, 30, 21, self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= play_state.player.dx
        self.y -= play_state.player.dy
        self.x += self.dx*self.speed
        self.y += self.dy*self.speed

        for i in range(len(game_world.objects[3])):
            if collide.collide_player(self,game_world.objects[3][i]):
                game_world.remove_object(self)
                game_world.objects[3][i].HP-=10

class circle_attack:
    def __init__(self):
        self.attack = load_image('circleat.png')
        self.power = 5
        self.x = 640
        self.y = 512
        self.timer = 0

    def get_bb(self):

        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self):

        self.attack.clip_draw(0, 0, 112, 112, self.x, self.y)
       # draw_rectangle(*self.get_bb())

    def update(self):
        for i in range(len(game_world.objects[3])):
            if collide.collide_player(self, game_world.objects[3][i]):
                if self.timer > 1:
                    game_world.objects[3][i].HP -= self.power
                    self.timer = 0

        self.timer += 0.2

class thunder:
    def __init__(self):
        self.image = load_image('thunder1.png')
        self.power = 10
        self.x = 640
        self.y = 512
        self.timer = 0
        self.frame =0
        if play_state.player.dir == 2:
            self.dir = 1
        elif play_state.player.dir == 3:
            self.dir = -1
        else:
            self.dir = 1
    def get_bb(self):
        return self.x + 20*self.dir, self.y - 20, self.x + 200*self.dir, self.y + 20
    def draw(self):
        if play_state.player.dir == 2:
            self.image.clip_draw(0, 19*self.frame, 98, 19, self.x+130*self.dir, self.y,200,50)
        elif play_state.player.dir == 3:
            self.image.clip_composite_draw(0, 19*self.frame, 98, 19, math.radians(180)," ",self.x+130*self.dir, self.y,200,50)
        else:
            self.image.clip_draw(0, 19 * self.frame, 98, 19, self.x + 130 * self.dir, self.y, 200, 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.timer >1.0:
            game_world.remove_object(self)

        for i in range(len(game_world.objects[3])):
            if collide.collide_player(self, game_world.objects[3][i]):
                   game_world.objects[3][i].HP -= self.power

        self.frame+=1
        self.timer += 0.2
