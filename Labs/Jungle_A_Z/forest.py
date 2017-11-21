from pico2d import *

class Forest:

    image = None

    def __init__(self):
        if Forest.image == None:
            Forest.image = load_image('./resource/Map.png')
        self.x, self.y = 980,980

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.x - 400, self.y - 400, 800,600,400,300)