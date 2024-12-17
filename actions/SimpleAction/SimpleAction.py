# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

# Import python modules
import os
from loguru import logger as log 
import string
import random

# Import gtk modules - used for the config rows
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class SimpleAction(ActionBase):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.has_configuration = True

    #     self.value = 0
    #     self.key_down_time: int = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    def on_ready(self):
        try:
            count = str(self.backend.get_count())
        except Exception as e:
            log.error(e)
            self.show_error()
            return
        
    # def on_key_down(self) -> None:
    #     self.set_center_label(str(self.value), font_size=30)
    #     randomLetter = random.choice(string.ascii_letters)

    #     settings = self.get_settings()
    #     settings["value"] = randomLetter
    #     self.set_settings(settings)
    #     self.value = "carlos"
    #     self.show_value()

    #     print("Key down")
    
    # def on_key_up(self) -> None:
    #     # self.set_center_label(str(self.value), font_size=30)
    #     # randomLetter = random.choice(string.ascii_letters)

    #     # settings = self.get_settings()
    #     # settings["value"] = randomLetter
    #     # self.value = randomLetter
    #     # self.set_settings(settings)
    #     # self.show_value()

    #     # print("Key down")
    #     self.set_center_label(str(self.backend.get_letter()))

    # def show_value(self) -> None:
    #     self.set_center_label(str(self.value), font_size=30)

    #     settings = self.get_settings()
    #     settings["value"] = self.value
    #     self.set_settings(settings)

    # def on_long_press(self):
    #     settings = self.get_settings()
    #     self.set_center_label(str(self.value), font_size=30)
    #     randomLetter = random.choice(string.ascii_letters)

    #     settings = self.get_settings()
    #     settings["value"] = randomLetter
    #     self.set_settings(settings)
        
    #     self.show_value()
        
    def get_count(self):
        return self.backend.get_count()
    