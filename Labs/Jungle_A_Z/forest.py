from pico2d import *

from tilemap import load_tile_map

class Forest:

    image = None
    TILE_SIZE = 48
    MAP_SIZE = 1920

    def __init__(self):
        self.mouse_x, self.mouse_y = 0, 0
        self.tile_map = load_tile_map('./resource/Jungle.json')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.tile_map.width * self.tile_map.tilewidth
        self.h = self.tile_map.height * self.tile_map.tileheight

    def update(self, x, y):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, self.max_window_left)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, self.max_window_bottom)

    def set_center_object(self, retsim):
        self.center_object = retsim
        self.max_window_left = self.w - self.canvas_width
        self.max_window_bottom = self.h - self.canvas_height

    def draw(self):
        self.tile_map.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height,0, 0)
        self.draw_tile_rect(*self.collision_tile(self.mouse_x, self.mouse_y))

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.mouse_x, self.mouse_y = event.x + self.center_object.x, (600 - event.y) + self.center_object.y


    def collision_tile(self, x,y):

        for i in range(400 + int(self.TILE_SIZE/2) , 400 + self.MAP_SIZE, self.TILE_SIZE):
            for j in range(300 + int(self.TILE_SIZE/2), 300 + self.MAP_SIZE, self.TILE_SIZE):
                left_b, bottom_b, right_b, top_b = i - 24, j - 24, i + 24, j + 24
                if x <= right_b and x >= left_b and y >= bottom_b and y <= top_b:
                    return i - self.center_object.x, j - self.center_object.y

        return 0, 0

    def draw_tile_rect(self, x, y):
        draw_rectangle(x - self.TILE_SIZE/2 , y - self.TILE_SIZE/2, x + self.TILE_SIZE/2, y + self.TILE_SIZE/2)