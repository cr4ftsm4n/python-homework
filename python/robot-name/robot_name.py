import random
from datetime import datetime


class Robot(object):
    def __init__(self):
        self.reset()

    def name(self):
        return self.name

    def reset(self):
        name = []
        random.seed(datetime.now())
        name.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        name.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        name.append(random.choice("1234567890"))
        name.append(random.choice("1234567890"))
        name.append(random.choice("1234567890"))
        self.name = "".join(name)
