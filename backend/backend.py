from streamcontroller_plugin_tools import BackendBase

import string
import random

class Backend(BackendBase):
    def __init__(self):
        super().__init__()

        self.counter: str = "XYZ"

    #def get_count(self) -> str:
    def get_letter(self) -> str:
        return random.choice(string.ascii_letters)

    #def increase_count(self) -> None:
    def random_letter(self) -> None:
        self.counter = random.choice(string.ascii_letters)

backend = Backend()
