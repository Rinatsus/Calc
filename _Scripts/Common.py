from Calculator import *
from Config import *


class Common(Calculator):
    def __init__(self):
        super(Common, self).__init__()
        self.set_name(NAME + COMMON)

