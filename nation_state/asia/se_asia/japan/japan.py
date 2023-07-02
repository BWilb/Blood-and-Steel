leaders = {
    "1910" : "Katsura Tarō",
    "1914" : "Ōkuma Shigenobu",
    "1918" : "Hara Takashi",
    "1932" : "Saitō Makoto",
    "1936" : "Kōki Hirota",
    "1939" : "Kiichirō Hiranuma"
}

population = {
    "1910": 49600000,
    "1914": 52500000,
    "1918": 55000000,
    "1932": 66300000,
    "1936": 70400000,
    "1939": 72500000
}
class Japan:
    def __init__(self, year):
        self.leader = leaders[year]
        self.population = population[year]
        # leader isn't initialized until time_frame is established.

    def printmetrics(self):
        print(self.population)

def main(time):
    japan = Japan(time)
    print(japan.population)