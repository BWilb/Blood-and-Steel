from datetime import datetime, timedelta
from game.ai import playable_nation
from datetime import datetime, timedelta
import json as js
from globe_relations import globe
#from nation_data.convert_coords import convert_coords

def establish_foreign_nations(globe, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function"""
    for i in range(0, len(args)):
        globe.nations.append(args[i])

leaders = {
    "1910" : "Paul Eyschen",
    "1914" : "Paul Eyschen",
    "1918" : "Léon Kauffman",
    "1932" : "Pierre Dupong",
    "1936" : "Pierre Dupong",
    "1939" : "Pierre Dupong"
}
monarchs = {
    "1910" : "Guillaume IV",
    "1914" : "Marie-Adélaïde",
    "1918" : "Marie-Adélaïde",
    "1932" : "Charlotte",
    "1936" : "Charlotte",
    "1939" : "Charlotte"
}

population = {
    "1910": 22597037,
    "1914": 24602624,
    "1918": 26713539,
    "1932": 35498876,
    "1936": 38735746,
    "1939": 41036654
}
gdp = {
    "1910": 4659663720,
    "1914": 4847024746,
    "1918": 4953286406,
    "1932": 5037403509,
    "1936": 5228000000,
    "1939": 7037894737
}

flags = {
    "1910": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1914": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1918": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1932": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1936": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1939": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg"
}

leader_images = {"1910": "../leaders/luxembourg/paul_eyschen_accroche_1910-1914.jpg",
                 "1914": "../leaders/luxembourg/paul_eyschen_accroche_1910-1914.jpg",
                 "1918": "../leaders/luxembourg/Léon_Kauffman_(1869-1952)_1918.jpg",
                 "1932": "../leaders/luxembourg/Joseph_Bech_(detail)_1933.jpg",
                 "1936": "../leaders/luxembourg/Pierre_Dupong,_Benelux_conference_The_Hague_March_1949,_Luxembourg_Delegation_1939.jpg",
                 "1939": "../leaders/luxembourg/Pierre_Dupong,_Benelux_conference_The_Hague_March_1949,_Luxembourg_Delegation_1939.jpg"
                 }

class Luxembourg(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Kingdom of Luxembourg"
        # date variables
        self.date = datetime(globe.date.year, 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        """Stability"""
        self.stability = 95.56
        # economic
        self.e_s = "recovery"
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        self.alliance = ""
        # coordinates
        self.lux_coords = []
        # other
        self.chosen = False
    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        """for i in range(len(nation_json['countries'])):
            if nation_json['countries'][i]['nation_name'] == "Luxembourg":
                for index, row in (nation_json['countries'][i]['coordinates']):

                    self.lux_coords.append(convert_coords(index, row))"""
        return self.lux_coords