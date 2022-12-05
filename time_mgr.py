import enemies
import attack
import my_ch
import game_world
import framework
import game_completed
from pico2d import*
class main_timer:
    def __init__(self):
        self.image = load_font('KO.TTF', 30)
        self.sec = 0
        self.minute=0
    def update(self):
        self.sec +=0.05
        if self.sec >60:
            self.minute+=1
            self.time=0

        if self.minute == 1:
            framework.change_state(game_completed)

        pass
    def draw(self):
        self.image.draw(640,950,f'{int(self.minute)}분{int(self.sec)}초',(255,255,255))