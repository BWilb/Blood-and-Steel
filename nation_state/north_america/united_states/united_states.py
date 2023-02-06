import random
from datetime import timedelta, datetime
from nation_state.europe.germany.germany import *
from nation_state.europe.italy.italy import *
from nation_state.europe.france.france import *
from nation_state.europe.britain.britain import *
from nation_state.europe.russia.russia import *
from nation_state.asia.japan.japan import *
from menu import options_menu
import globe
import keyboard

on_going_conflicts = []
"""variable established for any conflicts occurring"""
pop_difference = 0

leader_options = ["Justify War Goal",
                  "Disband Congress",
                  "Dissolve Congress",
                  "Call Congress to order",
                  "Switch Parties",
                  "Veto Bill",
                  "Make Executive Order"]

congressional_options = ["Declare War",
                         "Impose Sanctions",
                         "Propose Bill",
                         "Investigate Company",
                         "Impeach President",
                         "Remove President"]

judicial_options = ["Declare President Unconstitutional",
                    "Declare Congress Unconstitutional"]

historical_leaders = {
    "1910" : "William Howard Taft",
    "1914" : "Woodrow Wilson",
    "1918" : "Woodrow Wilson",
    "1932" : "Herbert Hoover",
    "1936" : "Franklin D. Roosevelt",
    "1939" : "Franklin D. Roosevelt"
}
communist_party_leaders = {
    "1910" : "C. E. Ruthenberg",
    "1914" : "C. E. Ruthenberg",
    "1918" : "C. E. Ruthenberg",
    "1932" : "William Z. Foster",
    "1936" : "Earl Browder",
    "1939" : "Earl Browder"
}

nationalist_leaders = {
    "1910" : "Theodore Roosevelt",
    "1914" : "Theodore Roosevelt",
    "1918" : "Theodore Roosevelt",
    "1932" : "Heinz Spanknöbel",
    "1936" : "Douglass MacArthur",
    "1939" : "Douglass MacArthur"
}

socialist_leaders = {
    "1910" : "Eugene V Debs",
    "1914" : "Eugene V Debs",
    "1918" : "Eugene V Debs",
    "1932" : "Morris Hillquit",
    "1936" : "Clarence Senior",
    "1939" : "Norman Thomas"
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
                       "Socialist Party USA", "American Freedom Party", "Republican Party", "Democratic Party"]

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

def random_events(us, time):
    parties = ["Democratic", "Republic"]
    random_number = random.randrange(0, 1000)
    if random_number % 2 == 0:
        # random event of civilians winning lottery
        print("One of your civilians won the lottery...Yay!!")
    elif random_number % 20 == 0:
        # random event of senator dying
        choice = random.randrange(0, len(parties))
        if choice == 0:
            print(f"Oh no a {parties[choice]} senator has died.")
        elif choice == 1:
            print(f"Oh no a {parties[choice]} senator has died.")

        choice = random.randrange(0, len(parties))
        if choice == 0:
            print(f"A {parties[choice]} senator has replaced the old.")
        elif choice == 1:
            print(f"A {parties[choice]} has replaced the old.")

    elif (random_number % 50 and int(time) >= 1945) or us.at_war:
        """Random event of nuclear attack.
        pre-emptive strike if not at war
        """
        print("You've been struck with a nuclear weapon...OH SHIT!!!")
        people_killed = random.randrange(1000, 10000000)
        us.population -= people_killed
        print(f"{people_killed} people died in a nuclear raid")
        
def show_statistics(nation, time):
    # shows statistics of the current state of the nation
    if nation.at_war:
        print(f"The current year is {time}.\n"
              f"Your current country is {nation.nation_name}.\n"
              f"Your current leader is {nation.leader}\n"
              f"Your current political party is {nation.political_party}"
              f"Your current population is {nation.population}\n"
              f"Your nation's current stability is {nation.stability}%.\n"
              f"Your nation is currently at war!\n"
              f"There are {nation.democratic_supporters} democrats.\n"
              f"There are {nation.republican_supporters} republicans.\n"
              f"There are {nation.nationalist_supporters} nationalists.\n"
              f"There are {nation.socialist_supporters} socialists.\n"
              f"There are {nation.communist_supporters} communists.\n"
              f"There are {nation.non_alligned} people who are independent.")
    else:
        print(f"The current year is {time}.\n"
              f"Your current country is {nation.nation_name}.\n"
              f"Your current leader is {nation.leader}\n"
              f"Your current political party is {nation.political_party}\n"
              f"Your current population is {nation.population}\n"
              f"Your nation is currently not at war!\n"
              f"Your nation's current stability is {nation.stability}%.\n"
              f"There are {nation.democratic_supporters} democrats.\n"
              f"There are {nation.republican_supporters} republicans.\n"
              f"There are {nation.nationalist_supporters} nationalists.\n"
              f"There are {nation.socialist_supporters} socialists.\n"
              f"There are {nation.communist_supporters} communists.\n"
              f"There are {nation.non_alligned} people who are independent.")

def us_collapse(us):
    print(f"Unfortunately your nation has collapsed due to low population.\n"
          f"{us.population} people remain.")
    us.stability = (us.stability - us.stability)
    # stability of United States collapses due to lack of population

def manual_game(us, year):
    print("Hi")
    date = datetime(int(year), 1, 1)
    # establishment of date variable
    germany = Germany(year)
    italy = Italy(year)
    #britain = Britain(year)
    russia = Russia(year)
    france = France(year)
    # establishment of European(partial) AIs
    japan = Japan(year)
    # establishment of Japanese (partial AI)
    """establishment of nations not chosen (based upon preset AI)"""
    globe_var = globe.Globe()


    show_statistics(us, year)

class UnitedStates:
    def __init__(self, year):
        self.leader = historical_leaders[year]
        self.population = population[year]
        self.political_party = political_parties[year]
        self.nation_name = "United States"
        """first 4 variables description of nation, not established until
        time frame chosen in opening menu file
        """
        if int(year) >= 1932:
            self.scotus_size = 9
        elif int(year) < 1932:
            self.scotus_size = 7
        self.representative_size = 435
        if int(year) > 1945:
            self.senate_size = 100
        elif int(year) < 1945:
            self.senate_size = 48
        if int(year) > 1945:
            self.defcon = 5
        self.stability = 92
        self.leader_popularity = 95
        self.goverment_type = "Republic"
        # stability, type, and popularity of nation and parties

        if self.political_party.lower() == "democratic":
            self.democratic_supporters = self.population * 0.85
            self.republican_supporters = (self.population - self.democratic_supporters) * 0.75
            self.communist_supporters = (self.population - (self.democratic_supporters + self.republican_supporters)) * 0.3
            self.socialist_supporters = (self.population - (self.democratic_supporters + self.republican_supporters +
                                                            self.communist_supporters)) * 0.2
            self.nationalist_supporters = (self.population - (self.democratic_supporters + self.republican_supporters +
                                                            self.communist_supporters + self.socialist_supporters)) * 0.5
            self.non_alligned = (self.population - (self.democratic_supporters + self.republican_supporters +
                                                            self.communist_supporters + self.socialist_supporters +
                                                    self.nationalist_supporters))
        elif self.political_party.lower() == "republican":
            self.republican_supporters = (self.population) * 0.85
            self.democratic_supporters = (self.population - self.republican_supporters) * 0.75
            self.communist_supporters = (self.population - (
                        self.democratic_supporters + self.republican_supporters)) * 0.3
            self.socialist_supporters = (self.population - (self.democratic_supporters + self.republican_supporters +
                                                            self.communist_supporters)) * 0.2
            self.nationalist_supporters = (self.population - (self.democratic_supporters + self.republican_supporters +
                                                              self.communist_supporters + self.socialist_supporters)) * 0.5
            self.non_alligned = (self.population - (self.democratic_supporters + self.republican_supporters +
                                                    self.communist_supporters + self.socialist_supporters +
                                                    self.nationalist_supporters))
        """
            population proportioned by political parties.
            main two are obviously republican and democrat.
            fringe parties are also involved
        """
        self.at_war = False
        self.nations_at_war_with = []
        self.german_relations = 100
        self.english_relations = 100
        self.french_relations = 100
        self.italian_relations = 100
        self.russian_relations = 100
        self.japanese_relations = 100
        # foreign relations

def main(time):
    united_states = UnitedStates(time)
    #print(united_states.leader)
    #show_statistics(united_states, time)
    manual_game(united_states, time)