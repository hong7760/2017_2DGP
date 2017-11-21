
from pico2d import *

class Retsim:
    image = None

    DOWN, LEFT, UP, RIGHT = 0, 1, 2, 3
    RUN = False
    def __init__(self):
        self.x, self.y = 400, 300
        self.frame = 0
        self.state = self.DOWN
        self.RUN = False
        if Retsim.image == None:
            Retsim.image = load_image('./resource/Retsim.png')

    def handle_left_run(self):
        if self.RUN == True:
            self.frame = (self.frame + 1) % 4
            self.x -= 5

    def handle_up_run(self):
        if self.RUN == True:
            self.frame = (self.frame + 1) % 4
            self.y += 5

    def handle_down_run(self):
        if self.RUN == True:
            self.frame = (self.frame + 1) % 4
            self.y -= 5

    def handle_right_run(self):
        if self.RUN == True:
            self.frame = (self.frame + 1) % 4
            self.x += 5

    handle_state = {
        LEFT: handle_left_run,
        RIGHT: handle_right_run,
        UP: handle_up_run,
        DOWN: handle_down_run
    }

    def update(self):
        self.handle_state[self.state](self)

    def draw(self):
        self.image.clip_draw(self.state * 48, 48 * self.frame, 48,48, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = self.LEFT
            self.RUN = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
            self.state = self.DOWN
            self.RUN = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
            self.state = self.UP
            self.RUN = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            self.state = self.RIGHT
            self.RUN = True

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            if self.state == self.LEFT:
                self.RUN = False
                self.frame = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_s):
            if self.state == self.DOWN:
                self.RUN = False
                self.frame = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_w):
            if self.state == self.UP:
                self.RUN = False
                self.frame = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_d):
            if self.state == self.RIGHT:
                self.RUN = False
                self.frame = 0
