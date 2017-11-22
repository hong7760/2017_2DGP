from pico2d import *

class Forest:

    image = None
    TILE_SIZE = 48
    MAP_SIZE = 1920
    def __init__(self):
        if Forest.image == None:
            Forest.image = load_image('./resource/Map.png')
        self.x, self.y = 960,960
        self.mouse_x, self.mouse_y = 0, 0

    def update(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def draw(self):
        self.image.clip_draw(self.x - 400, self.y - 300, 800,600,400,300)
        self.draw_tile_rect(*self.collision_tile(self.mouse_x, self.mouse_y))

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.mouse_x, self.mouse_y = event.x + self.x, (600 - event.y) + self.y

    def collision_tile(self, x,y):

        for i in range(400 + int(self.TILE_SIZE/2) , 400 + self.MAP_SIZE, self.TILE_SIZE):
            for j in range(300 + int(self.TILE_SIZE/2), 300 + self.MAP_SIZE, self.TILE_SIZE):
                left_b, bottom_b, right_b, top_b = i - 24, j - 24, i + 24, j + 24
                if x <= right_b and x >= left_b and y >= bottom_b and y <= top_b:
                    return i - self.x, j - self.y

        return 0, 0

    def draw_tile_rect(self, x, y):
        draw_rectangle(x - self.TILE_SIZE/2 , y - self.TILE_SIZE/2, x + self.TILE_SIZE/2, y + self.TILE_SIZE/2)