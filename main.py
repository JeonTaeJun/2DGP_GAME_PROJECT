from pico2d import *
import player
import enemies

running=True
open_canvas()
ground = load_image('MAP1.png')
pico2d.resize_canvas(1280, 1024)

skeltons = [enemies.skeleton() for i in range(11)]

player = player.my_player()

while running:
    clear_canvas()
    ground.draw(640, 550, 1280, 1024)
    player.update()
    player.draw()
    for skelton in skeltons:
        skelton.update(player.player_x, player.player_y)
    for skelton in skeltons:
         skelton.draw()
    update_canvas()
    for skelton in skeltons:
        skelton.frame=(skelton.frame + 1) % 6
    delay(0.05)


close_canvas()