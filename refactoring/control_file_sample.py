def handle_insignificant_growth(self):
    if len(self.long_term_memory[0]['Domestic Decisions']['Population']) > 0:
        if self.political_typology == "Democratic" or self.political_ideology == "Autocratic":
            pass
        else:
            pass

def handle_extreme_growth(self):
    if len(self.long_term_memory[0]['Domestic Decisions']['Population']) > 0:
        if self.political_typology == "Democratic" or self.political_ideology == "Autocratic":
            pass
        else:
            pass

def handle_stable_growth(self):
    if len(self.long_term_memory[0]['Domestic Decisions']['Population']) > 0:
        if self.political_typology == "Democratic" or self.political_ideology == "Autocratic":
            pass
        else:
            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Population"][0]['Stable growth occurrences']:
                if self

def determine_population_decision(self, domestic_issue):
    if domestic_issue.values() == "extreme growth":
        self.handle_extreme_growth()

    elif domestic_issue.values() == "stable growth":
        self.handle_stable_growth()

    elif domestic_issue.values() == "insignificant growth":
        self.handle_insiginificant_growth()