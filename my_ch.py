from pico2d import*
import collide
import game_world
import framework
import gameover
class my_player:
    def __init__(self):
        self.character = load_image('characters_.png')
        self.player_x = 1280 // 2
        self.player_y = 1024 // 2
        self.dx=0
        self.dy=0
        self.dir =0
        self.frame = 0
        self.HP = 100
    def get_bb(self):
        return self.player_x-10,self.player_y-15,self.player_x+10,self.player_y+15
    def draw(self):

        if self.dx==0 and self.dy==0:
            if self.dir ==2: #오른쪽
                self.character.clip_draw(0, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)
            else: #왼쪽
                self.character.clip_draw(0, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)

        elif self.dx>0:
            self.character.clip_draw(self.frame * 28, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)

        elif self.dx<0:
            self.character.clip_draw(self.frame * 28, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)

        elif self.dy!=0:
            if self.dir ==3:
                self.character.clip_draw(self.frame * 28, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)
            else:
                self.character.clip_draw(self.frame * 28, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 1) % 7

        for i in range(len(game_world.objects[3])):
            if collide.collide_player(self,game_world.objects[3][i]):
                self.HP-=game_world.objects[3][i].power
        print(self.HP)

        if self.HP<0:
            framework.change_state(gameover)
