for relation in self.improving_relations:
    """looping through nations that nation is currently improving relations with"""
    for nation in self.foreign_relations['foreign relations'][0]['nation']:
        """looping through nations in foreign relations book of nation"""
        if nation == relation:
            """checking if nation in book matches with nation that current nation is improving relations with"""
            if (self.foreign_relations['foreign relations'][0]["relations"] + 1.5) < 100:
                self.foreign_relations['foreign relations'][0]["relations"] += 1.5

            else:
                self.political_exponent += 0.25
                for i in range(0, len(self.objectives['objectives'][1]['foreign'])):
                    if (f"improve relations with {nation}") == self.objectives['objectives'][1]['foreign'][i]:
                        self.objectives['objectives'][1]['foreign'].pop(
                            self.objectives['objectives'][1]['foreign'][i])
                        self.objectives['objectives'][1]['foreign'].append(
                            f"create alliance with {self.foreign_relations['foreign relations'][0]['nation'].name}")

for relation in self.worsening_relations:
    """looping through nations that nation is currently worsening relations with"""
    for nation in self.foreign_relations['foreign relations'][0]['nation']:
        """looping through nations in foreign relations book of nation"""
        if nation.name == relation:
            """checking if nation in book matches with nation that current nation is worsening relations with"""
            if (self.foreign_relations['foreign relations'][0]["relations"] - 1.5) > -100:
                self.foreign_relations['foreign relations'][0]["relations"] -= 1.5

                for foreign_nation in foreign_nations:

                    if self.foreign_relations['foreign relations'][0]["relations"] < -25 and (
                            self.political_typology not in
                            foreign_nation.political_typology):
                        "poor relations with specific nation that isn't of similar ideology"
                        (self.objectives['objectives'][1]['foreign'].
                        append(
                            f"develop war goal against {self.foreign_relations['foreign relations'][0]['nation'].name}"))

                    else:
                        (self.objectives['objectives'][1]['foreign'].
                        append(
                            f"Improve relations with {self.foreign_relations['foreign relations'][0]['nation name']}"))

self.check_relations_status(foreign_nations)