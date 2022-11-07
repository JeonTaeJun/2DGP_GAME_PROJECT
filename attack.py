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
        self.dx=0
        self.dy=0
        self.dir=0
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
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= play_state.player.dx
        self.y -= play_state.player.dy
        self.x += self.speed

        for i in range(len(game_world.objects[3])):
            if collide.collide_player(self,game_world.objects[3][i]):
                game_world.remove_object(self)
                game_world.objects[3][i].HP-=self.power

class circle_attack:
    def __init__(self):
        self.attack = load_image('circleat.png')
        self.power = 5
        self.x = 640
        self.y = 512

    def get_bb(self):

        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self):

        self.attack.clip_draw(0, 0, 112, 112, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        for i in range(len(game_world.objects[3])):
            if collide.collide_player(self, game_world.objects[3][i]):
                game_world.objects[3][i].HP -= self.power
        pass