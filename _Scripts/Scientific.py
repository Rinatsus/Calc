from Calculator import *
from Config import *


class Scientific(Calculator):
    def __init__(self):
        super(Scientific, self).__init__()
        self.set_name(NAME + SCIENTIFIC)
