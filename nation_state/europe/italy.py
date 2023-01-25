leaders = {
    "1910" : "Luigi Luzzatti",
    "1914" : "Antonio Salandra",
    "1918" : "Vittorio Emanuele Orlando",
    "1932" : "Benito Mussolini",
    "1936" : "Benito Mussolini",
    "1939" : "Benito Mussolini"
}

population = {
    "1910": 36100000,
    "1914": 36500000,
    "1918": 36800000,
    "1932": 41000000,
    "1936": 42400000,
    "1939": 43500000
}
class Italy:
    def __init__(self, year):
        self.leader = leaders[year]
        self.population = population[year]
        # leader isn't initialized until time_frame is established.

    def printmetrics(self):
        print(self.population)