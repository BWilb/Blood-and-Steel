from collections import OrderedDict
from datetime import datetime
class Globe:
    def __init__(self, year):
        self.tension = 0
        self.date = datetime(int(year), 1, 1)
        self.nations = []