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

                    for allies in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                        if ("ally" or "friend" in foreign_nation.foreign_relations['foreign relations'][allies][
                            'relation status']):

                            for potential_ally in globe.nations:
                                if (potential_ally.name == foreign_nation.foreign_relations['foreign relations'][allies][
                                    'nation name'] and self.political_typology not in potential_ally.political_typology):

                                    for foreign_memories in potential_ally.long_term_memory["Foreign influence"]:
                                        if not f"{self.political_typology} Influence" in foreign_memories:
                                            potential_ally.long_term_memory["Foreign influence"].append({
                                                f"{self.political_typology} Influence": [
                                                    {
                                                        "Expiration date": globe.date + timedelta(days=30)
                                                    }
                                                ]
                                            })
                                            if not network.has_edge(self.name, foreign_nation.name):
                                                network.add_edge(self.name, foreign_nation.name)
                                            self.political_power -= 50

                elif action == "worsen relations" and self.political_power >= 15:
                    chance = random.randrange(1, 40)

                    if chance % 6 == 4:
                        for worsening in self.worsening_relations:
                            if not foreign_nation.name in worsening['nation name']:
                                if len(self.worsening_relations) < 10:
                                    if not network.has_edge(self.name, foreign_nation.name):
                                        network.add_edge(self.name, foreign_nation.name)

                                    self.worsening_relations.append({
                                        "nation name": foreign_nation.name,
                                        "duration": globe.date + timedelta(days=20)
                                    })
                                    self.political_power -= 15
                                    self.political_exponent -= 0.15

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

            elif (f"Establish ties with {foreign_nation.name}" or f"Improve relations with {foreign_nation.name}" in
                  self.objectives["objectives"][0]['foreign']):
                potential_actions = ["Form alliance", "Increase exports", "Increase imports", "Guarantee independence",
                                     "Improve relations"]
                action = potential_actions[random.randrange(0, len(potential_actions))]

                if action == "Form alliance" and self.political_power >= 60:
                    for foreign_relation in range(0, len(self.foreign_relations['foreign relations'])):
                        if (self.foreign_relations['foreign relations'][foreign_relation]['nation name'] ==
                        foreign_nation.name):
                            """Searching through foreign relations to find name of foreign nation"""
                            for for_relation in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                                """Searching through specific foreign nation's foreign relations"""
                                if (foreign_nation.foreign_relations['foreign relations'][for_relation]['nation name'] ==
                                self.name):
                                    """Searching for specific nation interacting with foreign nations"""

                                    if ("" in foreign_nation.foreign_relations['foreign relations'][for_relation]['alliance'] and
                                        "" not in self.foreign_relations['foreign relations'][foreign_relation]['alliance']):
                                        foreign_nation.foreign_relations['foreign relations'][for_relation]['alliance'] = (
                                            self.foreign_relations)['foreign relations'][foreign_relation]['alliance']
                                        self.political_power -= 60
                                        if not network.has_edge(self.name, foreign_nation.name):
                                            network.add_edge(self.name, foreign_nation.name)

                                    elif ("" not in foreign_nation.foreign_relations['foreign relations'][for_relation]['alliance'] and
                                    "" in self.foreign_relations['foreign relations'][foreign_relation]['alliance']):
                                        self.foreign_relations['foreign relations'][foreign_relation]['alliance'] = (
                                            foreign_nation.foreign_relations)['foreign relations'][for_relation]['alliance']
                                        self.political_power -= 60
                                        if not network.has_edge(self.name, foreign_nation.name):
                                            network.add_edge(self.name, foreign_nation.name)

                                    elif ("" not in foreign_nation.foreign_relations['foreign relations'][for_relation]['alliance'] and
                                    "" not in self.foreign_relations['foreign relations'][foreign_relation]['alliance']):
                                        foreign_nation.foreign_relations['foreign relations'][for_relation]['alliance'] = \
                                            f"{self.name}-{foreign_nation.name} alliance"
                                        self.foreign_relations['foreign relations'][foreign_relation]['alliance'] = \
                                            f"{self.name}-{foreign_nation.name} alliance"
                                        self.political_power -= 60
                                        if not network.has_edge(self.name, foreign_nation.name):
                                            network.add_edge(self.name, foreign_nation.name)

                elif action == "Increase exports" and self.political_power >= 15:
                    self.exports += 25
                    foreign_nation.imports += 25
                    self.political_power -= 15

                elif action == "Increase imports" and self.political_power >= 15:
                    self.imports += 25
                    foreign_nation.exports += 25
                    self.political_power -= 15

                elif action == "Guarantee independence" and self.political_power >= 50:
                    for relations in self.foreign_relations['foreign relations']:
                        if relations['nation name'] == foreign_nation.name:
                            if not relations['guaranteeing independence']:
                                relations['guaranteeing independence'] = True
                                self.political_power -= 50
                                self.political_exponent -= 0.25

                                if not network.has_edge(self.name, foreign_nation.name):
                                    network.add_edge(self.name, foreign_nation.name)

                elif action == "Improve relations" and self.political_power >= 25:
                    for nation in self.improving_relations:
                        if foreign_nation.name not in nation['nation name']:

                            if len(self.improving_relations) < 10:
                                if not network.has_edge(self.name, foreign_nation.name):
                                    network.add_edge(self.name, foreign_nation.name)
                                self.improving_relations.append({"nation name": foreign_nation.name,
                                                                 "duration": globe.date + timedelta(days=20)})
                                self.political_power -= 25
                                self.political_exponent -= 0.15