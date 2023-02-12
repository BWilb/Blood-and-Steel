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

political_parties = {
    "1910" : "Social Democratic Party of Germany",
    "1914" : "Social Democratic Party of Germany",
    "1918" : "Social Democratic Party of Germany",
    "1932" : "National Socialist Workers Party",
    "1936" : "National Socialist Workers Party",
    "1939" : "National Socialist Workers Party",
}

class Germany:
    def __init__(self, time):
        self.leader = leaders[time]
        self.population = population[time]
        self.political_party = political_parties[time]

        if int(time) < 1918:
            self.nation_name = "German Empire"
            self.government_type = "Constitutional Monarchy"
            self.at_war = True
            self.stability = 95
        elif int(time) > 1918 and int(time) <= 1933:
            self.nation_name = "Weimar Republic"
            self.government_type = "Federal Republic"
            self.at_war = False
            self.stability = 85

        elif int(time) > 1933 and int(time) <= 1945:
            self.nation_name = "Third Reich"
            self.at_war = False
            self.government_type = "Fascist Dictatorship"
            self.stability = 90
        """Internal characteristics of nation"""

        self.nations_at_war_with = []
        self.american_relations = 100
        self.english_relations = 100
        self.french_relations = 100
        self.italian_relations = 100
        self.russian_relations = 100
        self.japanese_relations = 100

def main(time):
    germany = Germany(time)
    print(germany.population)