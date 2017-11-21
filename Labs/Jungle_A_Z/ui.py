
from pico2d import *

class Ui:

    bar_tool_image = None
    hp_bar_image = None
    stamina_bar_image = None
    cold_bar_image = None

    def __init__(self):
        if Ui.bar_tool_image == None:
            Ui.bar_tool_image = load_image('./resource/bar_tool.png')
        if Ui.hp_bar_image == None:
            Ui.hp_bar_image = load_image('./resource/hp_bar.png')
        if Ui.stamina_bar_image == None:
            Ui.stamina_bar_image = load_image('./resource/stamina_bar.png')
        if Ui.cold_bar_image == None:
            Ui.cold_bar_image = load_image('./resource/cold_bar.png')

        self.hp, self.stamina, self.cold = 100, 100, 100
        self.invisible = 0.6
        Ui.bar_tool_image.opacify(self.invisible)
        Ui.hp_bar_image.opacify(self.invisible)
        Ui.stamina_bar_image.opacify(self.invisible)
        Ui.cold_bar_image.opacify(self.invisible)

    def draw(self):
        self.bar_tool_image.draw(150,100)
        self.bar_tool_image.draw(400,100)
        self.bar_tool_image.draw(650,100)
        self.hp_bar_image.clip_draw(0,0,int(176 * self.hp / 100),17,150 - 88 + int(88 * self.hp / 100),100)
        self.stamina_bar_image.clip_draw(0,0,int(176 * self.stamina / 100),17,400 - 88 + int(88 * self.stamina / 100),100)
        self.cold_bar_image.clip_draw(0,0,int(176 * self.cold / 100),17,650 - 88 + int(88 * self.cold / 100),100)

    def update(self, retsim):
        self.set_status(*retsim.get_status())

    def set_status(self, hp, stamina, cold):
        self.hp = hp
        self.stamina = stamina
        self.cold = cold