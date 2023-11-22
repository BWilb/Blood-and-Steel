def check_improve_relations(self, globe):
    relations = self.improving_relations[:]
    for relation in relations:
        if globe.date > relation['Duration']:
            self.improving_relations.pop(relation)

def check_worsen_relations(self, globe):
    relations = self.worsening_relations[:]
    for relation in relations:
        if globe.date > relation["Duration"]:
            self.worsening_relations.pop(relation)