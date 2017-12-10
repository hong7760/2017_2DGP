from pico2d import *

import random

class Wolf:

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
        self.x, self.y = random.randint(0, 2000), random.randint(0, 2000)
        self.frame = 0
        self.state = self.DOWN
        self.run = False
        self.total_frames = 0.0
        self.hp = 0
        if Wolf.image == None:
            Wolf.image = load_image('./resource/wolf.png')

    def update(self, frame_time):
        pass

    def draw(self):
        pass

    def handle_event(self,event):
        pass