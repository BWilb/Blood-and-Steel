for objective in self.objectives['objectives'][0]['domestic'][0]['population objectives']:
    if objective == "Maintain low population growth":
        if chance % 10 == 6 or chance % 15 == 2:
            killings = self.population * 0.001
            self.population -= killings
            self.deaths += killings