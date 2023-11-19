import random
from datetime import timedelta

def handle_depression(self, depress_sum):
    if depress_sum >= 4:
        actions = ['Decrease Corporate Taxes', "Decrease Income Taxes", "Increase Exports", "Decrease Imports"]
        action = actions[random.randrange(0, len(actions))]
        if action == 'Decrease Corporate Taxes':
            self.investment += 35

        elif action == "Decrease Income Taxes":
            self.consumer_spending += 25

        elif action == "Increase Exports":
            self.exports += 100

        elif action == "Decrease Imports":
            self.imports -= 10

def handle_negative_growth(self, issue, globe):
    recess_sum = 0
    depress_sum = 0
    recess_found = False
    # variable designed for finding recoveries in decisions
    depress_found = False
    # variable designed for finding expansions in decisions
    if len(self.long_term_memory[0]["Domestic Decisions"]['Economic']) > 0:
        for decision in self.long_term_memory[0]["Domestic Decisions"]['Economic']:
            if decision['Issue'] == "Recession" and issue == "Recession":
                recess_found = True
                for date in range(0, len(decision['Date'])):
                    if date >= 1 and (decision['Date'][date - 1] + timedelta(days=120)) == globe.date:
                        recess_sum += 1
                        if 3 <= recess_sum < 6 and not self.e_s == EconomicState.RECESSION:
                            self.e_s = EconomicState.RECESSION

                        elif recess_sum >= 6:
                            self.e_s = EconomicState.DEPRESSION
                    else:
                        break

            elif decision['Issue'] == "Depression" and issue == "Depression":
                recess_found = True
                for date in range(0, len(decision['Date'])):
                    if date >= 1 and (decision['Date'][date - 1] + timedelta(days=120)) == globe.date:
                        depress_sum += 1
                        self.handle_depression(depress_sum)

                    else:
                        break

        if not recess_found and issue == "Recession":
            self.long_term_memory[0]["Domestic Decisions"]['Economic'].append({
                "Issue": issue,
                "Date": [globe.date]
            })

        if not depress_found and issue == "Depression":
            self.long_term_memory[0]["Domestic Decisions"]['Economic'].append({
                "Issue": issue,
                "Date": [globe.date]
            })
    else:
        self.long_term_memory[0]['Domestic Decisions']['Economic'].append({
            "Issue": issue,
            "Date": [globe.date]
        })

def handle_expansion(self, expan_sum):
    if expan_sum >= 4:
        actions = ['Increase taxes', "Decrease government spending", "increase corporate taxes"]
        action = actions[random.randrange(0, len(actions))]
        if action == "Increase taxes":
            self.consumer_spending -= 25

        elif action == "Decrease government spending":
            self.government_spending -= 35

        elif action == "increase corporate taxes":
            self.investment -= 45

def handle_positive_growth(self, issue, globe):
    recov_sum = 0
    expan_sum = 0
    recov_found = False
    # variable designed for finding recoveries in decisions
    expan_found = False
    # variable designed for finding expansions in decisions
    if len(self.long_term_memory[0]["Domestic Decisions"]['Economic']) > 0:
        # checking length of domestic economic decisions
        for decision in self.long_term_memory[0]["Domestic Decisions"]['Economic']:
            if decision['Issue'] == "Recovery" and issue == "Recovery":
                recov_found = True
                for date in range(0, len(decision['Date'])):
                    if date >= 1 and (decision['Date'][date - 1] + timedelta(days=120)) == globe.date:
                        recov_sum += 1

                        if 3 < recov_sum < 6 and not self.e_s == EconomicState.RECOVERY:
                            self.e_s = EconomicState.RECOVERY

                        elif recov_sum == 6:
                            self.e_s = EconomicState.EXPANSION

                    else:
                        break

            if decision['Issue'] == "Expansion" and issue == "Expansion":
                expan_found = True
                for date in range(0, len(decision['Date'])):
                    if date >= 1 and (decision['Date'][date - 1] + timedelta(days=120)) == globe.date:
                        expan_sum += 1
                        self.handle_expansion(expan_sum)

                    else:
                        break

        if not recov_found and issue == "Recovery":
            self.long_term_memory[0]["Domestic Decisions"]['Economic'].append({
                "Issue": issue,
                "Date": [globe.date]
            })

        if not expan_found and issue == "Expansion":
            self.long_term_memory[0]["Domestic Decisions"]['Economic'].append({
                "Issue": issue,
                "Date": [globe.date]
            })

    else:
        self.long_term_memory[0]["Domestic Decisions"]['Economic'].append({
            "Issue": issue,
            "Date": [globe.date]
        })

def check_economic_growth(self, globe):
    if self.globe.date > self.economic_change_date:
        growth = ((self.current_gdp - self.past_gdp) / (self.current_gdp + self.past_gdp) / 2) * 100
        if growth <= 1.95:
            if self.e_s == EconomicState.RECESSION:
                self.handle_positive_growth("Recession", globe)

            if self.e_s == EconomicState.DEPRESSION:
                self.handle_positive_growth("Depression", globe)

        elif growth >= 6.95:
            if self.e_s == EconomicState.RECOVERY:
                self.handle_positive_growth("Recovery", globe)

            if self.e_s == EconomicState.EXPANSION:
                self.handle_positive_growth("Expansion", globe)

    else:
        self.check_economic_state(globe)