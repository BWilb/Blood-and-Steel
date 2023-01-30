leaders = {
    "1910" : "Wilhelm II",
    "1914" : "Wilhelm II",
    "1918" : "Friedrich Ebert",
    "1932" : "Paul Von Hindenburg",
    "1936" : "Adolf Hitler",
    "1939" : "Adolf Hitler"
}

population = {
    "1910": 63200000,
    "1914": 63200000,
    "1918": 62400000,
    "1932": 67200000,
    "1936": 69100000,
    "1939": 70500000
}
class Germany:
    def __init__(self, time):
        self.leader = leaders[time]
        self.population = population[time]
        # leader isn't initialized until time_frame is established.

def main(time):
    germany = Germany(time)
    print(germany.population)