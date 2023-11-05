import random
from datetime import timedelta

def democratic_international_decision(self, globe, network, user_nation):
    for foreign_nation in globe.nations:
        if self.name == foreign_nation.name or user_nation.name == foreign_nation.name:
            continue

        else:
            if self.political_power >= 10:

                if f"Challenge {foreign_nation.name}" in self.objectives["objectives"][0]['foreign']:
                    potential_actions = ["incursion into sphere of influence", "worsen relations", "embargo",
                               "spark democratic protests"]

                    action = potential_actions[random.randrange(0, len(potential_actions))]

                    if action == "incursion into sphere of influence":
                        for allies in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                            # searching through foreign nation's list of foreign relations
                            if "ally" or "friend" in foreign_nation.foreign_relations['foreign relations'][allies][
                                    'relation status']:

                                for potential_ally in globe.nations:
                                    if potential_ally.name == foreign_nation.foreign_relations['foreign relations'][allies][
                                        'nation name'] and "Democratic" not in potential_ally.political_typology:
                                        # checking if nation name matches with ally name and that ally is not democratic
                                        for foreign_memories in potential_ally.long_term_memory["Foreign influence"]:
                                            if not "Democratic Influence" in foreign_memories:
                                                potential_ally.long_term_memory["Foreign influence"].append({
                                                    "Democratic Influence": [
                                                        {
                                                            "Expiration date": globe.date + timedelta(days=30)
                                                        }
                                                    ]
                                                })
                                                self.political_power -= 10
                                                break

                    elif action == "worsen relations":
                        chance = random.randrange(1, 40)
                        if chance % 6 == 4:
                            for worsening in self.worsening_relations:
                                if foreign_nation.name in worsening['nation name']:
                                    self.worsening_relations['duration'] += timedelta(days=20)
                                    break

                                else:
                                    if len(self.worsening_relations) < 10:
                                        if not network.has_edge(self.name, foreign_nation.name):
                                            network.add_edge(self.name, foreign_nation.name)

                                        self.worsening_relations.append({
                                            "nation name": foreign_nation.name,
                                            "duration": globe.date + timedelta(days=20)
                                        })
                                        self.political_power -= 10
                                        self.political_exponent -= 0.15
                                        break

                    elif action == "spark democratic protests":
                        chance = random.randrange(1, 40)
                        if chance % 6 == 4:
                            foreign_nation.political_decision({
                                "Issue": "Liberal protest"
                            })

                elif (f"Establish ties with {foreign_nation.name}" or f"Improve relations with {foreign_nation.name}" in
                            self.objectives["objectives"][0]['foreign']):
                    potential_actions = ["Form alliance", "Increase exports", "Increase imports", "Guarantee independence",
                               "Improve relations"]
                    action = potential_actions[random.randrange(0, len(potential_actions))]

                    if action == "Form alliance":
                        # action generated to form alliance
                        for relations in self.foreign_relations['foreign relations']:
                            # searching through nation's foreign relations
                            if relations['nation name'] == foreign_nation.name:
                                # checking if foreign nation name equal to foreign nation name
                                for nations in foreign_nation.foreign_relations['foreign relations']:
                                    # searching through nations in foreign nation's foreign relations
                                    if self.name == nations['nation name']:
                                        # checking if nation's name is equal to nation in foreign nation's foreign relations
                                        if "" not in relations['alliance'] and "" in nations["alliance"]:
                                            nations['alliance'] = relations['alliance']

                                        elif "" in relations['alliance'] and "" not in nations['alliance']:
                                            relations['alliance'] = nations['alliance']

                                        else:
                                            pass

                    elif action == "Increase exports":
                        self.exports += 25
                        foreign_nation.imports += 25

                    elif action == "Increase imports":
                        self.imports += 25
                        foreign_nation.exports += 25

                    elif action == "Guarantee independence":
                        for relations in self.foreign_relations['foreign relations']:
                            if relations['nation name'] == foreign_nation.name:
                                if not relations['guaranteeing independence']:
                                    relations['guaranteeing independence'] = True

                                    if not network.has_edge(self.name, foreign_nation.name):
                                        network.add_edge(self.name, foreign_nation.name)

                    elif action == "Improve relations":
                        for nation in self.improving_relations:
                            if foreign_nation.name in nation['nation name']:
                                nation['duration'] += timedelta(days=20)

                            else:
                                if len(self.improving_relations) < 10:
                                    if not network.has_edge(self.name, foreign_nation.name):
                                        network.add_edge(self.name, foreign_nation.name)
                                        self.improving_relations.append({"nation name": foreign_nation.name,
                                                                         "duration": globe.date + timedelta(days=20)})