
from pico2d import *

class Ui:

    bar_tool_image = None
    hp_bar_image = None
    stamina_bar_image = None
    cold_bar_image = None

    inven_image = None
    inven_on_mouse_image = None
    INVENTORY_SIZE = 8
    def __init__(self):
        self.invisible = 0.6
        self.set_ui_image()
        self.set_inventory_image()
        self.hp, self.stamina, self.cold = 100, 100, 100
        self.active_inventory = False


    def draw(self):
        self.bar_draw()

    def update(self, retsim):
        self.set_status(*retsim.get_status())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_TAB):
            if self.active_inventory:
                self.active_inventory = False
            else:
                self.active_inventory = True


    def set_status(self, hp, stamina, cold):
        self.hp = hp
        self.stamina = stamina
        self.cold = cold

    def set_ui_image(self):
        if Ui.bar_tool_image == None:
            Ui.bar_tool_image = load_image('./resource/bar_tool.png')
        if Ui.hp_bar_image == None:
            Ui.hp_bar_image = load_image('./resource/hp_bar.png')
        if Ui.stamina_bar_image == None:
            Ui.stamina_bar_image = load_image('./resource/stamina_bar.png')
        if Ui.cold_bar_image == None:
            Ui.cold_bar_image = load_image('./resource/cold_bar.png')

    def set_inventory_image(self):
        if Ui.inven_image == None:
            Ui.inven_image = load_image('./resource/inven_idle.png')
        if Ui.inven_on_mouse_image == None:
            Ui.inven_on_mouse_image = load_image('./resource/inven_on_mouse.png')

        Ui.inven_on_mouse_image.opacify(self.invisible)
        Ui.inven_image.opacify(self.invisible)

    def bar_draw(self):
        self.bar_tool_image.draw(150, 100)
        self.hp_bar_image.clip_draw(0, 0, int(176 * self.hp / 100), 17, 150 - 88 + int(88 * self.hp / 100), 100)

        self.bar_tool_image.draw(400, 100)
        self.stamina_bar_image.clip_draw(0, 0, int(176 * self.stamina / 100), 17,
                                         400 - 88 + int(88 * self.stamina / 100), 100)

        self.bar_tool_image.draw(650, 100)
        self.cold_bar_image.clip_draw(0, 0, int(176 * self.cold / 100), 17, 650 - 88 + int(88 * self.cold / 100), 100)

        Ui.bar_tool_image.opacify(self.invisible)
        Ui.hp_bar_image.opacify(self.invisible)
        Ui.stamina_bar_image.opacify(self.invisible)
        Ui.cold_bar_image.opacify(self.invisible)

    def draw_inventory(self):
        pass