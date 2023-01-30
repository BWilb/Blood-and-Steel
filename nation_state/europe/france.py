leaders = {
    "1910" : "Armand Fallières",
    "1914" : "Raymond Poincaré",
    "1918" : "Raymond Poincaré",
    "1932" : "Paul Von Hindenburg",
    "1936" : "Albert Lebrun",
    "1939" : "Albert Lebrun"
}

population = {
    "1910": 40300000,
    "1914": 39600000,
    "1918": 38700000,
    "1932": 40700000,
    "1936": 40400000,
    "1939": 40300000
}
class France:
    def __init__(self, year):
        self.leader = leaders[year]
        self.population = population[year]
        # leader isn't initialized until time_frame is established.

def main(time):
    france = France(time)
    print(france.population)