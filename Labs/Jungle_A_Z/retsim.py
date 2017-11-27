
from pico2d import *

class Retsim:

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4
    image = None

    DOWN, LEFT, UP, RIGHT = 0, 1, 2, 3
    def __init__(self):
        self.x, self.y = 960, 960
        self.frame = 0
        self.state = self.DOWN
        self.run = False
        self.total_frames = 0.0
        self. hp, self.stamina, self.cold = 100,100,100
        if Retsim.image == None:
            Retsim.image = load_image('./resource/Retsim.png')

    def handle_left_run(self, frame_time):
        if self.run == True:
            self.total_frames += Retsim.TIME_PER_ACTION * Retsim.FRAMES_PER_ACTION * frame_time
            self.frame = int(self.total_frames) % 4
            self.x = max(400, self.x - Retsim.RUN_SPEED_PPS * frame_time)

    def handle_up_run(self, frame_time):
        if self.run == True:
            self.total_frames += Retsim.TIME_PER_ACTION * Retsim.FRAMES_PER_ACTION * frame_time
            self.frame = int(self.total_frames) % 4
            self.y = min(1620, self.y + Retsim.RUN_SPEED_PPS * frame_time)

    def handle_down_run(self, frame_time):
        if self.run == True:
            self.total_frames += Retsim.TIME_PER_ACTION * Retsim.FRAMES_PER_ACTION * frame_time
            self.frame = int(self.total_frames) % 4
            self.y = max(300, self.y - Retsim.RUN_SPEED_PPS * frame_time)

    def handle_right_run(self, frame_time):
        if self.run == True:
            self.total_frames += Retsim.TIME_PER_ACTION * Retsim.FRAMES_PER_ACTION * frame_time
            self.frame = int(self.total_frames) % 4
            self.x = min(1520, self.x + Retsim.RUN_SPEED_PPS * frame_time)

    handle_state = {
        LEFT: handle_left_run,
        RIGHT: handle_right_run,
        UP: handle_up_run,
        DOWN: handle_down_run
    }

    def get_pos(self):
        return self.x, self.y

    def get_status(self):
        return self.hp, self.stamina, self.cold

    def update(self, frame_time):
        self.handle_state[self.state](self, frame_time)
        self.hp -= frame_time * 10
        self.stamina -= frame_time * 10
        self.cold -= frame_time * 10

    def draw(self):
        self.image.clip_draw(self.state * 48, 48 * self.frame, 48,48, 400, 300)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = self.LEFT
            self.run = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
            self.state = self.DOWN
            self.run = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
            self.state = self.UP
            self.run = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            self.state = self.RIGHT
            self.run = True

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            if self.state == self.LEFT:
                self.run = False
                self.frame = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_s):
            if self.state == self.DOWN:
                self.run = False
                self.frame = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_w):
            if self.state == self.UP:
                self.run = False
                self.frame = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_d):
            if self.state == self.RIGHT:
                self.run = False
                self.frame = 1
