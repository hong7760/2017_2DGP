import random
import json
import os

from pico2d import *

import game_framework
import title_state
from retsim import Retsim
from forest import Forest
name = "MainState"


font = None



def enter():
    open_canvas(sync= True)
    global forest
    global retsim
    retsim = Retsim()
    forest = Forest()

def exit():
    global retsim, forest
    del(retsim)
    del(forest)
    close_canvas()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            else:
                retsim.handle_event(event)


def update():
    retsim.update()
    forest.update()

def draw():
    clear_canvas()
    forest.draw()
    retsim.draw()
    update_canvas()

def pause_draw():
    pass