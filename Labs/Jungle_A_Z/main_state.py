import random
import json
import os

from pico2d import *

import game_framework
import title_state
from retsim import Retsim
from forest import Forest
from ui import Ui
name = "MainState"


font = None



def enter():
    global forest, retsim, ui
    retsim = Retsim()
    forest = Forest()
    ui = Ui()

def exit():
    global retsim, forest, ui
    del(retsim)
    del(forest)
    del(ui)

def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            else:
                retsim.handle_event(event)
                forest.handle_event(event)


def update(frame_time):
    retsim.update(frame_time)
    forest.update(*retsim.get_pos())
    ui.update(retsim)

def draw(frame_time):
    clear_canvas()
    forest.draw()
    ui.draw()
    retsim.draw()
    update_canvas()

def pause_draw():
    pass