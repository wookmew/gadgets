import pygame
import random
import time

dead = 0
alive = 1
shield = 2

class Actor:
    '''
    Represents an Actor in the game. Can be the Player, a Monster, boxes, wall.
    Any object in the game's grid that appears on the stage, and has an
    x- and y-coordinate.
    '''

    def __init__(self, icon_file, stage, x, y, delay=5):
        '''
        (Actor, str, Stage, int, int, int) -> None
        Given the name of an icon file (with the image for this Actor),
        the stage on which this Actor should appear, the x- and y-coordinates
        that it should appear on, and the speed with which it should
        update, construct an Actor object.
        '''

        self._icon = pygame.image.load(icon_file)  # the image image to display of self
        self.set_position(x, y)  # self's location on the stage
        self._stage = stage  # the stage that self is on

        # the following can be used to change this Actors 'speed' relative to other
        # actors speed. See the delay method.
        self._delay = delay
        self._delay_count = 0

    def set_position(self, x, y):
        '''
        (Actor, int, int) -> None
        Set the position of this Actor to the given x- and y-coordinates.
        '''

        (self._x, self._y) = (x, y)

    def get_position(self):
        '''
        (Actor) -> tuple of two ints
        Return this Actor's x and y coordinates as a tuple.
        '''

        return (self._x, self._y)

    def get_icon(self):
        '''
        (Actor) -> pygame.Surface
        Return the image associated with this Actor.
        '''

        return self._icon

    def is_dead(self):
        '''
        (Actor) -> bool
        Return True iff this Actor is not alive.
        '''
        self.set_position(0, 0)
        # pygame.mixer.music.load('sound/gameover.mp3')
        # pygame.mixer.music.play(1)
        return False

    def move(self, other, dx, dy):
        '''
        (Actor, Actor, int, int) -> bool

        Other is an Actor telling us to move in direction (dx, dy). In this case, we just move.
        (dx,dy) is in {(1,1), (1,0), (1,-1), (0,1), (0,0), (0,-1), (-1,1), (-1,0), (-1,-1)}
    
        In the more general case, in subclasses, self will determine 
        if they will listen to other, and if so, will try to move in
        the specified direction. If the target space is occupied, then we 
        may have to ask the occupier to move.
        '''

        self.set_position(self._x + dx, self._y + dy)
        return True

    def random_move(self):
        '''
        Let's actor random move
        :return:
        '''
        return random.choice([-1, 1])

    def delay(self):
        '''
        (Actor) -> bool
        Manage self's speed relative to other Actors. 
        Each time we get a chance to take a step, we delay. If our count wraps around to 0
        then we actually do something. Otherwise, we simply return from the step method.
        '''
        self._delay_count = (self._delay_count + 1) % self._delay
        return self._delay_count == 0

    def step(self):
        '''
        (Actor) -> None
        Make the Actor take a single step in the animation of the game.
        self can ask the stage to help as well as ask other Actors
        to help us get our job done.
        '''

        pass


class Player(Actor):
    '''
    A Player is an Actor that can handle events. These typically come
    from the user, for example, key presses etc.
    '''

    def __init__(self, icon_file, stage, x=0, y=0):
        '''
        (Player, str, Stage, int, int) -> None
        Construct a Player with given image, on the given stage, at
        x- and y- position.
        '''

        super().__init__(icon_file, stage, x, y)

    def handle_event(self, event):
        '''
        Used to register the occurrence of an event with self.
        '''

        pass


class KeyboardPlayer(Player):
    '''
    A KeyboardPlayer is a Player that can handle keypress events.
    '''

    def __init__(self, icon_file, stage, x=0, y=0):
        '''
        Construct a KeyboardPlayer. Other than the given Player information,
        a KeyboardPlayer also keeps track of the last key event that took place.
        '''

        super().__init__(icon_file, stage, x, y)
        self._last_event = None  # we are only interested in the last event
        self.attr = 'player'
        self.status = alive

    def handle_event(self, event):
        '''
        (KeyboardPlayer, int) -> None
        Record the last event directed at this KeyboardPlayer.
        All previous events are ignored.
        '''

        self._last_event = event

    def step(self):
        '''
        (KeyboardPlayer) -> None
        Take a single step in the animation. 
        For example: if the user asked us to move right, then we do that.
        '''

        if self._last_event is not None and self.status:
            dx, dy = None, None
            if self._last_event == pygame.K_DOWN:
                dx, dy = 0, 1
            if self._last_event == pygame.K_LEFT:
                dx, dy = -1, 0
            if self._last_event == pygame.K_RIGHT:
                dx, dy = 1, 0
            if self._last_event == pygame.K_UP:
                dx, dy = 0, -1
            if self._last_event == pygame.K_q:
                dx, dy = -1, -1
            if self._last_event == pygame.K_w:
                dx, dy = 1, -1
            if self._last_event == pygame.K_a:
                dx, dy = -1, 1
            if self._last_event == pygame.K_s:
                dx, dy = 1, 1
            if dx is not None and dy is not None:
                self.move(self, dx, dy)  # we are asking ourself to move

            self._last_event = None

    def move(self, other, dx, dy):
        '''
        (Actor, Actor, int, int) -> bool
        Move this Actor by dx and dy, if possible. other is the Actor that asked to make this move.
        If a move is possible (a space is available) then move to it and return True.
        If another Actor is occupying that space, ask that Actor to move to make space, and then
        move to that spot, if possible.
        If a move is not possible, then return False.
        '''

        # Where we are supposed to move. 
        new_x = self._x + dx
        new_y = self._y + dy

        # FIX THIS ACCORDING TO LAB INSTRUCTIONS IN PART 1
        # TODO: Check if (new_x, new_y) is on the stage.
        #       If it is, then determine if another Actor is occupying that spot. If so,
        #       self asks them to move. If they moved, then we can occupy the spot. Otherwise
        #       we can't move. We return True if we moved and False otherwise.

        # Judging the boundary
        if not self._stage.is_in_bounds(new_x, new_y):
            return False

        # Judging the target attribute
        # oh. wall
        if self._stage.what_is(new_x, new_y) == 2:
            return False

        # Judging the goal
        target = self._stage.get_actor(new_x, new_y)
        if isinstance(target, list):
            print(1234)
            for item in target:
                # Release monster
                if item.attr == 'monster':
                    item.times -= 1000
                # Sticky box move
                if item.attr == 'sticky box':
                    item.move(other, dx, dy)
                    return False
        elif target:
            if target.attr == 'monster':
                if target.skill == 'angel':
                    selfstatus = shield
                    pygame.mixer.music.load('sound/heart.mp3')
                    pygame.mixer.music.play(1)
                    target.status = dead  # angel dead
                    target.set_position(-1, -1)
                else:
                    if self.status == shield:
                        self.status = alive
                        pygame.mixer.music.load('sound/gameover.mp3')
                        pygame.mixer.music.play(1)
                        return False
                    else:
                        self.is_dead()
                        # self.status = dead
                        pygame.mixer.music.load('sound/gameover.mp3')
                        pygame.mixer.music.play(1)
                        return False

            flag = target.move(other, dx, dy)
            if not flag:
                return False

        pygame.mixer.music.load('sound/jump.mp3')
        pygame.mixer.music.play(1)
        super().move(other, dx, dy)
        return True


class Box(Actor):
    '''
    A Box Actor.
    '''

    def __init__(self, icon_file, stage, x=0, y=0, attr='box'):
        '''
        (Actor, str, Stage, int, int) -> None
        Construct a Box on the given stage, at given position.
        '''

        super().__init__(icon_file, stage, x, y)
        self.attr = attr
        self.status = ''

    def move(self, other, dx, dy):
        '''
        (Actor, Actor, int, int) -> bool
        Move this Actor by dx and dy, if possible. other is the Actor that asked to make this move.
        If a move is possible (a space is available) then move to it and return True.
        If another Actor is occupying that space, ask that Actor to move to make space, and then
        move to that spot, if possible.
        If a move is not possible, then return False.
        '''

        new_x = self._x + dx
        new_y = self._y + dy

        # FIX THIS ACCORDING TO LAB INSTRUCTIONS IN PART 1
        # TODO:
        # If (new_x, new_y) is on the stage, and is empty, then 
        # we simply move there. Otherwise, we ask whomever is at (new_x, new_y)
        # to move, also the same direction. If they moved, the space is now
        # empty, so we now move into (new_x, new_y). If we successfully
        # moved, then we return True, otherwise, we return False. '''

        # Judging the boundary
        if not self._stage.is_in_bounds(new_x, new_y):
            return False

        # Judging the target attribute
        singal = self._stage.what_is(new_x, new_y)
        if singal != 1:
            return False

        target = self._stage.get_actor(new_x, new_y)
        if isinstance(target, list):
            for item in target:
                # Release monster
                if item.attr == 'monster':
                    item.times -= 1000
                # Sticky box move
                if item.attr == 'sticky box':
                    item.move(other, dx, dy)
                    return False
        elif target and (target.attr == 'box' or target.attr == 'sticky box'):
            flag = target.move(other, dx, dy)
            if not flag:
                return False
            else:
                super().move(other, dx, dy)
                return True
        elif target:
            if target.attr == 'monster' and self.attr == 'sticky box' and target.skill != 'ghost':
                target.times += 1000
                super().move(other, dx, dy)
                return False

        super().move(other, dx, dy)

        return True

    def is_dead(self):
        self.set_position(-1, -1)
        return False


# COMPLETE THIS CLASS FOR PART 2 OF LAB
class Wall(Actor):
    '''
    A Wall actor and Wall is fixed
    '''

    def __init__(self, icon_file, stage, x=0, y=0):
        '''
        (Actor, str, Stage, int, int) -> None
        Construct a Box on the given stage, at given position.
        '''

        super().__init__(icon_file, stage, x, y)
        self.attr = 'wall'


class Monster(Actor):
    '''A Monster class.'''

    def __init__(self, icon_file, stage, x=0, y=0, delay=5, attr='monster', skill=''):
        '''Construct a Monster.'''
        super().__init__(icon_file, stage, x, y, delay)
        self.attr = attr
        self.status = alive
        self.skill = skill
        self.times = int(time.time())

    def step(self):
        '''
        Take one step in the animation (this Monster moves by one space). If it's being delayed, return None. Else, return True.
        '''

        if not self.delay() and self.status:
            _dx = self.random_move()
            _dy = self.random_move()
            return self.move(self, _dx, _dy)
        return True


    def move(self, other, dx, dy):
        '''
        (Actor, Actor, int, int) -> bool
        Move this Actor by dx and dy, if possible. other is the Actor that asked to make this move. If a move is possible (a space is available) then move to it and return True.
        If another Actor is occupying that space, or if that space is out of bounds,
        bounce back in the opposite direction.
        If a bounce back happened, then return False.
        '''

        if other != self:  # Noone pushes me around
            return False

        bounce_off_edge = False
        new_x = self._x + dx
        new_y = self._y + dy
        # print(dx, dy, new_x, new_y, self._x, self._y)

        if not self._stage.is_in_bounds_x(new_x):
            self._dx = - dx
            bounce_off_edge = True
        if not self._stage.is_in_bounds_y(new_y):
            self._dy = - dy
            bounce_off_edge = True
        if bounce_off_edge:
            return False

        # FIX THIS FOR PART 3 OF THE LAB
        # MONSTERS SHOULD BOUNCE BACK FROM BOXES AND OTHER MONSTERS # HINT: actor = self._stage.get_actor(new_x,new_y)
        actor = self._stage.get_actor(new_x, new_y)
        if isinstance(actor, list):
            dx = 0
            dy = 0
            # Judging the death of the monster
            if self.is_dead():
                return False
        elif actor != None:
            if actor.attr != 'player' and actor.attr != 'sticky box':
                dx = 0
                dy = 0
                # Judging the death of the monster
                if self.is_dead():
                    return False
            elif actor.attr == 'sticky box' and self.skill != 'ghost':  # monster paralyzed
                self.times += 1000
                return super().move(other, dx, dy)
            else:
                if int(time.time()) > self.times:  # monster can kill player
                    if self.skill == 'angel':
                        actor.status = shield
                        pygame.mixer.music.load('sound/heart.mp3')
                        pygame.mixer.music.play(1)
                        self.set_position(-1, -1)
                        self.status = dead
                    elif actor.status == shield:
                        self.status = alive
                        pygame.mixer.music.load('sound/gameover.mp3')
                        pygame.mixer.music.play(1)
                        return False
                    else:
                        #actor.status = dead
                        if actor.is_dead():
                            pygame.mixer.music.load('sound/gameover.mp3')
                            pygame.mixer.music.play(1)
                            return False

        if int(time.time()) > self.times:  # monster can't move
            return super().move(other, dx, dy)
        else:
            return False

    def is_dead(self):
        '''
        Return whether this Monster has died.
        That is, if self is surrounded on all sides, by either Boxes or other Monsters.
        '''

        # TODO: This is part of the assignment and not yet required for the lab.
        #  If you have extra time in lab, feel free to get working on this.
        filter = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
        target_pos = [(self._x - x, self._y - y) for x, y in filter]
        target_boom = []
        for pos in target_pos:
            pos_x, pos_y = pos
            if pos_x == self._x and pos_y == self._y:
                continue
            actor = self._stage.get_actor(pos_x, pos_y)
            if isinstance(actor, list):
                return False
            elif actor and (actor.attr == 'box' or actor.attr == 'wall'):
                target_boom.append(actor)
                continue

            if not self._stage.is_in_bounds(pos_x, pos_y):
                continue

            return False

        self.set_position(-1, -1)
        self.status = dead

        if self.skill == 'boom':
            for item in target_boom:
                item.set_position(-1, -1)

        return True

class Stage:
    '''
    A Stage that holds all the game's Actors (Player, monsters, boxes, etc.).
    '''

    def __init__(self, width, height, icon_dimension):
        '''Construct a Stage with the given dimensions.'''

        self._actors = []  # all actors on this stage (monsters, player, boxes, ...)
        self._player = None  # a special actor, the player

        # the logical width and height of the stage
        self._width, self._height = width, height

        self._icon_dimension = icon_dimension  # the pixel dimension of all actors
        # the pixel dimensions of the whole stage
        self._pixel_width = self._icon_dimension * self._width
        self._pixel_height = self._icon_dimension * self._height
        self._pixel_size = self._pixel_width, self._pixel_height

        # get a screen of the appropriate dimension to draw on
        self._screen = pygame.display.set_mode(self._pixel_size)

    def is_in_bounds(self, x, y):
        '''
        (Stage, int, int) -> bool
        Return True iff the position (x, y) falls within the dimensions of this Stage.'''
        return self.is_in_bounds_x(x) and self.is_in_bounds_y(y)

    def is_in_bounds_x(self, x):
        '''
        (Stage, int) -> bool
        Return True iff the x-coordinate given falls within the width of this Stage.
        '''

        return 0 <= x and x < self._width

    def is_in_bounds_y(self, y):
        '''
        (Stage, int) -> bool
        Return True iff the y-coordinate given falls within the height of this Stage.
        '''

        return 0 <= y and y < self._height

    def what_is(self, x, y):
        target = self.get_actor(x, y)
        # print(target)
        if target and not isinstance(target, list):
            if target.attr == 'box':
                return 1
            elif target.attr == 'wall':
                return 2
            elif target.attr == 'monster':
                return 3

        return 1

    def get_width(self):
        '''
        (Stage) -> int
        Return width of Stage.
        '''

        return self._width

    def get_height(self):
        '''
        (Stage) -> int
        Return height of Stage.
        '''

        return self._height

    def set_player(self, player):
        '''
        (Stage, Player) -> None
        A Player is a special actor, store a reference to this Player in the attribute
        self._player, and add the Player to the list of Actors.
        '''

        self._player = player
        self.add_actor(self._player)

    def remove_player(self):
        '''
        (Stage) -> None
        Remove the Player from the Stage.
        '''

        self.remove_actor(self._player)
        self._player = None

    def player_event(self, event):
        '''
        (Stage, int) -> None
        Send a user event to the player (this is a special Actor).
        '''

        self._player.handle_event(event)

    def add_actor(self, actor):
        '''
        (Stage, Actor) -> None
        Add the given actor to the Stage.
        '''

        self._actors.append(actor)

    def remove_actor(self, actor):
        '''
        (Stage, Actor) -> None
        Remove the given actor from the Stage.
        '''

        self._actors.remove(actor)

    def step(self):
        '''
        (Stage) -> None
        Take one step in the animation of the game. 
        Do this by asking each of the actors on this Stage to take a single step.
        '''

        num = 0
        for a in self._actors:
            if a.attr == 'monster':
                num += 1
            a.step()
        if num == 0:
            pygame.quit()

    def get_actors(self):
        '''
        (Stage) -> None
        Return the list of Actors on this Stage.
        '''

        # target may overlap
        target = []
        for a in self._actors:
            if a.get_position() == (x, y):
                target.append(a)

        # target exists
        if target:
            if len(target) == 1:
                return target[0]
            else:
                return target

        return None

    def get_actor(self, x, y):
        '''
        (Stage, int, int) -> Actor or None
        Return the first actor at coordinates (x,y).
        Or, return None if there is no Actor in that position.
        '''

        target = []
        for a in self._actors:
            if a.get_position() == (x, y):
                target.append(a)

        # target exists
        if target:
            if len(target) == 1:
                return target[0]
            else:
                return target

        return None

    def draw(self):
        '''
        (Stage) -> None
        Draw all Actors that are part of this Stage to the screen.
        '''

        self._screen.fill((0, 0, 0))  # (0,0,0)=(r,g,b)=black
        for a in self._actors:
            icon = a.get_icon()
            (x, y) = a.get_position()
            d = self._icon_dimension
            rect = pygame.Rect(x * d, y * d, d, d)
            self._screen.blit(icon, rect)
        pygame.display.flip()
