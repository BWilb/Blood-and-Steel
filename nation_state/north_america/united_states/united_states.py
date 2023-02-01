from datetime import timedelta, datetime
from nation_state.europe.germany.germany import *
from nation_state.europe.italy.italy import *
from nation_state.europe.france.france import *
from nation_state.europe.britain.britain import *
from nation_state.europe.russia.russia import *
from nation_state.asia.japan.japan import *

on_going_conflicts = []
"""variable established for any conflicts occurring"""

leader_options = ["Justify War Goal",
                  "Impose Sanctions",
                  "Declare War",
                  "Disband Congress",
                  "Dissolve Congress",
                  "Switch Parties",
                  "Veto Bill",
                  "Make Executive Order"]

leaders = {
    "1910" : "William Howard Taft",
    "1914" : "Woodrow Wilson",
    "1918" : "Woodrow Wilson",
    "1932" : "Herbert Hoover",
    "1936" : "Franklin D. Roosevelt",
    "1939" : "Franklin D. Roosevelt"
}

population = {
    # population will be set up to increase or decrease randomly throughout every year
    "1910": 92410000,
    "1914": 99110000,
    "1918": 103210000,
    "1932": 124840000,
    "1936": 128050000,
    "1939": 130880000
}

alternative_parties = ["Libertarian Party", "Communist Party USA", "Trans-humanist party",
                       "Green Party", "Constitution Party", "Reform Party", "American Nazi Party"
                       "Socialist Party USA", "American Freedom Party"]

political_parties = {
    # elections will be implemented later on
    "1910" : "Republican",
    "1914" : "Democratic",
    "1918" : "Democratic",
    "1932" : "Republican",
    "1936" : "Democratic",
    "1939" : "Democratic"
}

vice_presidents = {
    # dictionary of vice presidents incase president gets assassinated
    "1910" : "James S. Sherman",
    "1914" : "Thomas R. Marshall",
    "1918" : "Thomas R. Marshall",
    "1932" : "Charles Curtis",
    "1936" : "John Garner",
    "1939" : "Henry Wallace"
}

def show_statistics(nation, time):
    # shows statistics of the current state of the nation
    if nation.at_war:
        print(f"The current year is {time}.\n"
              f"Your current country is {nation.nation_name}.\n"
              f"Your current leader is {nation.leader}\n"
              f"Your current political party is {nation.political_party}"
              f"Your current population is {nation.population}\n"
              f"Your nation is currently at war!")
    else:
        print(f"The current year is {time}.\n"
              f"Your current country is {nation.nation_name}.\n"
              f"Your current leader is {nation.leader}\n"
              f"Your current population is {nation.population}\n"
              f"Your nation is currently not at war!")

def manual_game(us, year):
    date = datetime(int(year), 1, 1)
    # establishment of date variable

    germany = Germany(year)
    italy = Italy(year)
    britain = Britain(year)
    russia = Russia(year)
    france = France(year)
    # establishment of European(partial) AIs
    japan = Japan(year)
    # establishment of Japanese (partial AI)
    """establishment of nations not chosen (based upon preset AI)"""

    i = 1
    while us.population > 1000:
        print(date)
        """while loop constraint based 
        upon assumption that US has large enough population"""
        #print(date + timedelta(days=i))

        i += 1
class UnitedStates:
    def __init__(self, year):
        self.leader = leaders[year]
        self.population = population[year]
        self.political_party = political_parties[year]
        self.nation_name = "United States"
        """first 4 variables description of nation, not established until
        time frame chosen in opening menu file
        """
        self.stability = 100
        # stability of nation
        self.at_war = False
        # foreign relations

def main(time):
    united_states = UnitedStates(time)
    print(united_states.population)
    # show_statistics(united_states, time)
    manual_game(united_states, time)
main("1939")