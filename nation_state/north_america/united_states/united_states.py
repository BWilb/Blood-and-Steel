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

alternative_parties = ["Libertarian Party", "Communist Party USA", "transhumanist party",
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
    if nation.at_war:
        print(f"The current year is {time}.\n"
              f"Your current country is {nation.nation_name}.\n"
              f"Your current leader is {nation.leader}\n"
              f"Your current population is {nation.population}\n"
              f"Your nation is currently at war!")
    else:
        print(f"The current year is {time}.\n"
              f"Your current country is {nation.nation_name}.\n"
              f"Your current leader is {nation.leader}\n"
              f"Your current population is {nation.population}\n"
              f"Your nation is currently not at war!")

class UnitedStates:
    def __init__(self, year):
        self.leader = leaders[year]
        self.population = population[year]
        # leader isn't initialized until time_frame is established.
        self.nation_name = "United States"
        self.at_war = False


def main(time):
    united_states = UnitedStates(time)
    print(united_states.population)
    show_statistics(united_states, time)