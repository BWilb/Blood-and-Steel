import random
from datetime import timedelta


def democratic_international_decision(self, foreign_nation_list, globe, network, user_nation):

    for foreign_nation in foreign_nation_list:
        if self.name != foreign_nation.name:
            if foreign_nation.name == user_nation.name:
                continue
            if self.political_power >= 10:

                if f"Challenge {foreign_nation.name}" in self.objectives["objectives"][0]['foreign'] or (
                        ("Democratic" or "Republicanism") not
                        in foreign_nation.political_typology):
                    actions = ["Incursion into sphere of influence", "worsen relations", "embargo",
                               "spark democratic protests"]
                    action = actions[random.randrange(0, len(actions))]
                    print(action)

                    if action == "Incursion into sphere of influence":
                        # checking if random action is incurring into foe's sphere of influence
                        for allies in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                            # searching through foreign nation's list of foreign relations
                            if "ally" or "friend" in foreign_nation.foreign_relations['foreign relations'][allies][
                                'relation status']:
                                # checking if in foreign relations, if a nation is a friend/ally
                                for potential_ally in foreign_nation_list:
                                    if potential_ally.name == foreign_nation.foreign_relations['foreign relations'][allies][
                                        'nation name']:
                                        """potential_ally.long_term_memory['Foreign influence'].append({"Democratic Influence": [
                                            {"Expiration date": globe.date + timedelta(days=30)}
                                        ]})"""
                                        pass

                    elif action == "worsen relations":
                        chance = random.randrange(1, 40)
                        if chance % 6 == 4:
                            if ("Democratic" or "Republicanism") not in foreign_nation.political_typology:
                                for worsening in range(0, len(self.worsening_relations)):
                                    if foreign_nation.name in self.worsening_relations[worsening]['nation name']:
                                        self.worsening_relations[worsening]['duration'] += timedelta(days=20)

                                    else:
                                        if len(self.worsening_relations) <= 10:
                                            if not network.has_edge(self.name, foreign_nation.name):
                                                network.add_edge(self.name, foreign_nation.name)
                                            self.worsening_relations.append({"nation name": foreign_nation.name,
                                                                             "duration": globe.date + timedelta(days=20)})

                    elif action == "embargo":
                        chance = random.randrange(1, 40)
                        if chance % 6 == 4:
                            if ("Democratic" or "Republicanism") not in foreign_nation.political_typology:
                                for foreign_relations in range(0, len(self.foreign_relations['foreign relations'])):
                                    if (self.foreign_relations["foreign relations"][foreign_relations][
                                        'nation name'] == foreign_nation.name):
                                        if not self.foreign_relations['foreign relations'][foreign_relations]['embargoed']:
                                            self.foreign_relations['foreign relations'][foreign_relations]['embargoed'] = True
                                            self.exports -= 25
                                            self.imports -= 25

                    elif action == "spark democratic protests":
                        chance = random.randrange(1, 40)
                        if chance % 6 == 4:
                            if ("Democratic" or "Republicanism") not in foreign_nation.political_typology:
                                foreign_nation.political_decision({"Issue": "Liberal protest"})
                                return True

                if ((f"Establish ties with {foreign_nation.name}" or f"Improve relations with {foreign_nation.name}") in
                        self.objectives["objectives"][0]['foreign'] or
                        ("Democratic" or "Republicanism") in foreign_nation.political_typology):
                    actions = ["Form alliance", "Increase exports", "Increase imports", "Guarantee independence",
                               "Improve relations"]
                    action = actions[random.randrange(0, len(actions))]
                    print(action)

                    if self.political_power >= 10:
                        if action == "Form alliance":
                            for nation in range(0, len(self.foreign_relations['foreign relations'])):
                                if (self.foreign_relations['foreign relations'][nation][
                                    'nation name'] == foreign_nation.name):
                                    if "" in foreign_nation.alliance and "" in self.alliance:
                                        if not network.has_edge(self.name, foreign_nation.name):
                                            network.add_edge(self.name, foreign_nation.name)
                                        self.foreign_relations['foreign relations'][nation][
                                            'alliance'] = f"{self.name}'s alliance"
                                        self.alliance = f"{self.name}'s alliance"

                                    elif "" in foreign_nation.alliance and f"{self.name}'s alliance":
                                        foreign_nation.alliance = f"{self.name}'s alliance"
                                        if not network.has_edge(self.name, foreign_nation.name):
                                            network.add_edge(self.name, foreign_nation.name)

                                    else:
                                        self.alliance = foreign_nation.alliance
                                        if not network.has_edge(self.name, foreign_nation.name):
                                            network.add_edge(self.name, foreign_nation.name)


                        elif action == "Increase exports":
                            self.exports += 25
                            foreign_nation.imports += 25

                        elif action == "Increase imports":
                            self.imports += 45
                            foreign_nation.exports += 45

                        elif action == "Guarantee independence":
                            for nation in range(0, len(self.foreign_relations['foreign relations'])):
                                if (self.foreign_relations['foreign relations'][nation][
                                    'nation name'] == foreign_nation.name and
                                        not self.foreign_relations['foreign relations'][nation]['guaranteeing independence']):
                                    if not network.has_edge(self.name, foreign_nation.name):
                                        network.add_edge(self.name, foreign_nation.name)
                                        self.foreign_relations['foreign relations'][nation][
                                            'guaranteeing independence'] = True
                                        self.political_exponent -= 0.15

                        elif action == "Improve relations":
                            for nation in self.improving_relations:
                                if foreign_nation.name in self.improving_relations[nation]['nation name']:
                                    self.improving_relations[nation]['duration'] += timedelta(days=20)

                                else:
                                    if len(self.improving_relations) <= 10:
                                        if not network.has_edge(self.name, foreign_nation.name):
                                            network.add_edge(self.name, foreign_nation.name)
                                            self.improving_relations.append({"nation name": foreign_nation.name,
                                                                             "duration": globe.date + timedelta(days=20)})
