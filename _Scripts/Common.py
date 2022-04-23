from Calculator import *


class Common(Calculator):
    def __init__(self, window):
        super(Common, self).__init__(window)
        self.set_name(NAME + COMMON)

