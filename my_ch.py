from pico2d import*

class my_player:
    def __init__(self):
        self.character = load_image('characters_.png')
        self.player_x = 1280 // 2
        self.player_y = 1024 // 2
        self.frame = 0
        self.HP = 100
    def get_bb(self):
        return self.player_x-15,self.player_y-20,self.player_x+15,self.player_y+20
    def draw(self,direction,move_x,move_y):
        if direction == 1:
            self.character.clip_draw(0, direction * 35, 27, 35, self.player_x, self.player_y, 40, 40)

        elif direction == 0:
            self.character.clip_draw(0, direction * 35, 27, 35, self.player_x, self.player_y, 40, 40)

        elif direction == 3:
            self.character.clip_draw(self.frame * 28, direction * 35, 27, 35, self.player_x, self.player_y, 40, 40)

        elif direction == 2:
            self.character.clip_draw(self.frame * 28, direction * 35, 27, 35, self.player_x, self.player_y, 40, 40)
        draw_rectangle(*self.get_bb())

    def update(self,move_x,move_y):
        self.frame = (self.frame + 1) % 7

        if self.player_x < 0:
            self.player_x += 15
        elif self.player_x > 1280:
            self.player_x -= 15

        if self.player_y < 0:
            self.player_y += 15
        elif self.player_y > 1000:
            self.player_y -= 15

        self.player_x += move_x * 10
        self.player_y += move_y * 10
