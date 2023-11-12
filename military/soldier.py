import random
from datetime import timedelta

class Soldier:
    def __init__(self, nation_of_origin, globe):
        self.fatherland = nation_of_origin
        # fatherland is where specific soldier is from
        self.monetary_cost = 222.50
        self.occupied_territory = []
        self.retiring_date = globe.date + timedelta(days=random.randrange(30, 180))