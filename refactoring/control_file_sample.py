import random
from datetime import timedelta


def make_international_decision(self, globe, network, user_nation):
    for foreign_nation in globe.nations:
        if self.name == foreign_nation.name or user_nation.name == foreign_nation.name:
            continue

        else:
            if (f"Challenge {foreign_nation.name}" or
                    f"Contain {foreign_nation.name}" in self.objectives["objectives"][0]['foreign']):
                potential_actions = ["incursion into sphere of influence", "worsen relations", "embargo",
                                     "spark protests"]

                action = potential_actions[random.randrange(0, len(potential_actions))]


                if action == "incursion into sphere of influence" and self.political_power >= 50:

                    for relation in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                        if (foreign_nation.foreign_relations['foreign relations'][relation]['relation status'] == "ally" and
                            self.political_typology not in
                                foreign_nation.foreign_relations['foreign relations'][relation]['nation'].political_typology):
                            for nation_search in globe.nations:
                                if nation_search.name == foreign_nation.foreign_relations['foreign relations'][relation]['nation'].name:
                                    for foreign_memories in range(0, len(nation_search.long_term_memory['Foreign influence'])):
                                        if not f"{self.political_typology} Influence" in nation_search.long_term_memory['Foreign influence'][foreign_memories]:
                                            nation_search.long_term_memory['Foreign influence'].append({
                                                f"{self.political_typology} Influence": [
                                                    {
                                                        "Expiration date": globe.date + timedelta(days=30)
                                                    }
                                                ]
                                            })
                                            self.political_power -= 50

                elif action == "worsen relations" and self.political_power >= 15:
                    chance = random.randrange(1, 40)

                    if chance % 6 == 4:
                        for worsening in self.worsening_relations:
                            if not foreign_nation.name in worsening['nation name']:
                                if len(self.worsening_relations) < 10:
                                    network.add_edge(self.name, foreign_nation.name)

                                self.worsening_relations.append({
                                    "nation name": foreign_nation.name,
                                    "duration": globe.date + timedelta(days=20)
                                })
                                self.political_power -= 15
                                self.political_exponent -= 0.15
                                break

                elif action == "spark protests" and self.political_power >= 25:
                    chance = random.randrange(1, 40)
                    if chance % 6 == 4:
                        if "Democratic" in self.political_typology:
                            foreign_nation.political_decision({
                                "Issue": "Liberal protest"
                            })

                        if "Fascist" in self.political_typology:
                            foreign_nation.political_decision({
                                "Issue": "Far right protest"
                            })

                        if "Communist" in self.political_typology:
                            foreign_nation.political_decision({
                                "Issue": "Far left protest"
                            })

                        if "Autocratic" in self.political_typology:
                            foreign_nation.political_decision({
                                "Issue": "Autocratic protest"
                            })
                        self.political_power -= 25
                        break