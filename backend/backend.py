from streamcontroller_plugin_tools import BackendBase

class Backend(BackendBase):
    def __init__(self):
        super().__init__()

        self.counter: int = 0

    def get_count(self) -> int:
        return self.counter

    def increase_count(self) -> int:
        self.counter += 1

backend = Backend()
