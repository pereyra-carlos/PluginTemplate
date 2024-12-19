from streamcontroller_plugin_tools import BackendBase

#import run_jenkins_job
import run_job_and_wait

import string
import random

class Backend(BackendBase):
    def __init__(self):
        super().__init__()

        self.counter: str = "XYZ"

    #def get_count(self) -> str:
    def get_letter(self) -> str:
        return random.choice(string.ascii_letters)
    
    def run_job_prod(self) -> str:
        #run_jenkins_job.ejecutar_job_en_jenkins()
        #return run_jenkins_job.ejecutar_job_en_jenkins()
        return run_job_and_wait.ejecutar_job_completo
    

    #def increase_count(self) -> None:
    def random_letter(self) -> None:
        self.counter = random.choice(string.ascii_letters)

backend = Backend()
