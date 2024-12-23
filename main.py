# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

# Import actions
from .actions.SimpleAction.SimpleAction import SimpleAction



import os

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Launch backend
        print("antes")
        #backend_path = os.path.join(self.PATH, "backend", "backend.py") 
        #self.launch_backend(backend_path=backend_path, open_in_terminal=True) 
        self.launch_backend(os.path.join(self.PATH, "backend", "backend.py"), os.path.join(self.PATH, "backend", ".venv"), open_in_terminal=False)
        print("despues")

        ## Register actions
        self.simple_action_holder = ActionHolder(
            plugin_base = self,
            action_base = SimpleAction,
            action_id = "dev_core447_Template::SimpleAction", # Change this to your own plugin id
            action_name = "Simple Action",
        )
        self.add_action_holder(self.simple_action_holder)

        # Register plugin
        self.register(
            plugin_name = "Template",
            github_repo = "https://github.com/pereyra-carlos/PluginTemplate",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )
