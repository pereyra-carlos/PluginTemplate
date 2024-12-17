from streamcontroller_plugin_tools import BackendBase 

import os
import string
import random

class Backend(BackendBase):
    def __init__(self):
        super().__init__()

        self.letter = "XYZ"

    def get_letter(self):
        self.letter = random.choice(string.ascii_letters) 
        return self.letter

    def random_letter(self):
        self.letter = random.choice(string.ascii_letters) 


backend = Backend()
