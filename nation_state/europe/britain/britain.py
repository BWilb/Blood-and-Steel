leaders = {
    """Dictionary for leaders
    Leader selection will be in sync with time frame selection
    Unlike population, leader dictionary will be setup to be as historically accurate as possible"""

    "1910": "George V",
    "1914": "George V",
    "1918": "George V",
    "1932": "Ramsey McDonald",
    "1936": "Stanley Baldwin",
    "1939": "Winston Churchill"
}

population = {
    """Dictionary for population
    Population selection will be in sync with time frame selection
    Population will then be set up to grow or shrink in random amounts"""

    "1910": 44915900,
    "1914": 42956900,
    "1918": 39582000,
    "1932": 46335000,
    "1936": 47081300,
    "1939": 46029200
}


class Britain:
    def __init__(self, time):
        self.leader = leaders[time]
        self.population = population[time]
        # leader isn't initialized until time_frame is established.


"""def main(time):
    britain = Britain(time)
    print(britain.population)"""
