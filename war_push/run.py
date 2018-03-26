import sys, pygame, random
from body import *
pygame.init()

ww=Stage(20, 20, 24)
ww.set_player(KeyboardPlayer("icons/face-cool-24.png", ww))

# Add Wall actor
# test monster dead

ww.add_actor(Wall("icons/wall.jpg", ww, 2, 2))
ww.add_actor(Wall("icons/wall.jpg", ww, 1, 2))
ww.add_actor(Wall("icons/wall.jpg", ww, 0, 2))
ww.add_actor(Wall("icons/wall.jpg", ww, 1, 3))
ww.add_actor(Wall("icons/wall.jpg", ww, 1, 5))
ww.add_actor(Wall("icons/wall.jpg", ww, 1, 6))
ww.add_actor(Wall("icons/wall.jpg", ww, 0, 4))
ww.add_actor(Wall("icons/wall.jpg", ww, 1, 4))
ww.add_actor(Wall("icons/wall.jpg", ww, 2, 4))

# Add Monster actor
# ww.add_actor(Monster("icons/face-devil-grin-24.png", ww, 0, 3, 2))  # test monster dead
ww.add_actor(Monster("icons/face-devil-grin-24.png", ww, 6, 3, 2))
ww.add_actor(Monster("icons/face-devil-grin-24.png", ww, 7, 4, 2))
ww.add_actor(Monster("icons/face-devil-grin-24.png", ww, 4, 10, 2))
ww.add_actor(Monster("icons/face-devil-grin-24.png", ww, 5, 20, 2))
ww.add_actor(Monster("icons/boom.png", ww, 5, 3, 2, 'monster', 'boom'))
ww.add_actor(Monster("icons/ghost.png", ww, 8, 6, 2, 'monster', 'ghost'))
ww.add_actor(Monster("icons/angel.png", ww, 3, 6, 2, 'monster', 'angel'))

# YOUR COMMENT GOES HERE. BRIEFLY DESCRIBE WHAT THE FOLLOWING LOOP DOES.
num_boxes=0
while num_boxes<100:
    x=random.randrange(ww.get_width())
    y=random.randrange(ww.get_height())
    if ww.get_actor(x,y) is None:
        if num_boxes < 70:
            ww.add_actor(Box("icons/emblem-package-2-24.png", ww, x, y))
        else:
            ww.add_actor(Box("icons/grenn-package-2-24.png", ww, x, y, 'sticky box'))
        num_boxes += 1

# YOUR COMMENT GOES HERE. BRIEFLY DESCRIBE WHAT THE FOLLOWING LOOP DOES.
# Top left is q
# Lower right is a
# Top left is w
# Lower right is s
while True:
    pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            ww.player_event(event.key)
    ww.step()
    ww.draw()
