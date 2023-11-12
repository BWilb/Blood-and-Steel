import random
from datetime import timedelta


def handle_protest(self, political_issue, globe):
    days = random.randrange(10, 30)
    if len(self.long_term_memory["Domestic Decisions"][0]["protests"]) > 0:
        for past_memory in self.long_term_memory["Domestic Decisions"][0]["protests"][political_issue.values()]["protest occurred"]['Protest ideology']:
            # looping through list of memories with protests
            if f"{political_issue.values()}" in past_memory:
                # checking if the ideology of the protest is in the memory
                if self.political_typology != political_issue.values():
                    # checking if own ideology is not similar to that of the protest
                    self.long_term_memory["Domestic Decisions"][0]["protests"][political_issue.values()]["protest occurred"]['Date'] += globe.date
                    self.long_term_memory["Domestic Decisions"][0]["protests"][political_issue.values()]["protest occurred"]['Duration'] += days

            else:
                self.long_term_memory["Domestic Decisions"][0]["protests"][f"{political_issue.values()}"].append({
                    "protest occurred": [
                        {"Protest ideology": f"{political_issue.values()}",
                         "Date": globe.date,
                         "Duration": globe.date + timedelta(days=days),
                         "Influence": round(random.uniform(0.01, 0.10), 2),
                         "Action taken": "none"}
                    ]
                })

    else:
        if not self.political_typology in political_issue.values():
            self.long_term_memory["Domestic Decisions"][0]["protests"][f"{political_issue.values()}"].append({
                "protest occurred": [
                    {"Protest ideology": f"{political_issue.values()}",
                     "Date": globe.date,
                     "Duration": globe.date + timedelta(days=days),
                     "Influence": round(random.uniform(0.01, 0.05), 2)
                     }
                ]
            })