import random
from datetime import timedelta


def make_positive_decision(self, globe, network, user_nation):
    for foreign_nation in globe.nations:
        if self.name == foreign_nation.name or user_nation.name == foreign_nation.name:
            continue

        else:
            if (f"Establish ties with {foreign_nation.name}" or f"Improve relations with {foreign_nation.name}" in
                    self.objectives["objectives"][0]['foreign']):
                potential_actions = ["Form alliance", "Increase exports", "Increase imports", "Guarantee independence",
                                     "Improve relations"]

                action = potential_actions[random.randrange(0, len(potential_actions))]
                if action == "Increase exports" and self.political_power >= 15:
                    self.exports += 25
                    foreign_nation.imports += 25
                    self.political_power -= 15
                    break

                elif action == "Increase imports" and self.political_power >= 15:
                    self.imports += 25
                    foreign_nation.exports += 25
                    self.political_power -= 15
                    break

                elif action == "Guarantee independence" and self.political_power >= 50:
                    for relations in self.foreign_relations['foreign relations']:
                        if relations['nation'].name == foreign_nation.name:
                            if not relations['guaranteeing independence']:
                                relations['guaranteeing independence'] = True
                                self.political_power -= 50
                                self.political_exponent -= 0.25

                                network.add_edge(self.name, foreign_nation.name)
                                break

                if action == "Improve relations" and self.political_power >= 25:
                    if foreign_nation.name not in [rel['nation name'] for rel in self.improving_relations]:
                        # Check if there's room for additional relations and the absence of a direct connection
                        # Add a new relation entry and adjust political attributes
                        if len(self.improving_relations) < 10:
                            self.improving_relations.append({
                                "nation name": foreign_nation.name,
                                "duration": globe.date + timedelta(days=20)
                            })

                            self.political_power -= 25
                            self.political_exponent -= 15

                            network.add_edge(self.name, foreign_nation.name)
                            break

                """if action == "Form alliance" and self.political_power >= 60:
                            for foreign_relation in range(0, len(self.foreign_relations['foreign relations'])):

                                if foreign_nation.name == self.foreign_relations['foreign relations'][foreign_relation][
                                    "nation"].name:
                                    for nation in range(0, len(foreign_nation.foreign_relations['foreign relations'])):

                                        if self.name == foreign_nation.foreign_relations['foreign relations'][nation]['nation'].name:

                                            if ("" in foreign_nation.foreign_relations['foreign relations'][nation][
                                                'alliance'] and "" in
                                                    self.foreign_relations['foreign relations'][foreign_relation]["alliance"]):

                                                self.foreign_relations['foreign relations'][foreign_relation]["alliance"] = \
                                                    f"{self.name}-{foreign_nation.name} alliance"

                                                foreign_nation.foreign_relations['foreign relations'][nation]['alliance'] = \
                                                    f"{self.name}-{foreign_nation.name} alliance"
                                                self.political_power -= 60
                                                foreign_nation.political_power -= 60

                                                if not network.has_edge(self.name, foreign_nation.name):
                                                    network.add_edge(self.name, foreign_nation.name)

                                            elif ("" not in foreign_nation.foreign_relations['foreign relations'][nation][
                                                'alliance'] and "" in
                                                  self.foreign_relations['foreign relations'][foreign_relation]["alliance"]):
                                                self.foreign_relations['foreign relations'][foreign_relation]["alliance"] = \
                                                    foreign_nation.foreign_relations['foreign relations'][nation]['alliance']
                                                self.political_power -= 60

                                                if not network.has_edge(self.name, foreign_nation.name):
                                                    network.add_edge(self.name, foreign_nation.name)"""
def make_negative_decision(self, globe, network, user_nation):
    for foreign_nation in globe.nations:
        if self.name == foreign_nation.name or user_nation.name == foreign_nation.name:
            continue

        else:
            potential_actions = ["incursion into sphere of influence", "worsen relations", "embargo",
                                 "spark protests"]

            action = potential_actions[random.randrange(0, len(potential_actions))]

            if action == 'worsen relations' and self.political_power >= 15:
                if len(self.worsening_relations) < 10:
                    if foreign_nation.name not in [rel['nation name'] for rel in self.worsening_relations]:
                        self.worsening_relations.append({
                            "nation name": foreign_nation.name,
                            "duration": globe.date + timedelta(days=20)
                        })
                        self.political_power -= 25
                        self.political_exponent -= 15
                        network.add_edge(self.name, foreign_nation.name)
                        break

            elif action == "spark protests" and self.political_power >= 25:
                chance = random.randrange(1, 40)
                if chance % 6 == 4:
                    if "Democratic" in self.political_typology:
                        foreign_nation.political_decision(
                            "Democratic protest", globe)

                    if "Fascist" in self.political_typology:
                        foreign_nation.political_decision("Fascist protest", globe)

                    if "Communist" in self.political_typology:
                        foreign_nation.political_decision("Communist protest", globe)

                    if "Autocratic" in self.political_typology:
                        foreign_nation.political_decision("Autocratic protest", globe)
                    self.political_power -= 25
                break

            elif action == "embargo":
                sum = 0
                for nation in self.foreign_relations['foreign relations']:
                    if nation['embargoed']:
                        sum += 1

                if sum < 12:
                    for nation in self.foreign_relations['foreign relations']:
                        if nation['nation'].name == foreign_nation.name and not nation['embargoed']:
                            nation['embargoed'] = True
                            print("jo")

def make_international_decision(self, globe, network, user_nation):
    self.make_negative_decision(self, globe, network, user_nation)
    self.make_positive_decision(self, globe, network, user_nation)

    self.check_improve_relations(globe)
    self.check_worsen_relations(globe)