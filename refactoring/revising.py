import random
from datetime import timedelta


def updating_ideology(self, globe):
    ideologies = ['Democratic', "Fascist", "Communist", "Autocratic"]
    for protest in self.long_term_memory['protests']:
        # looping through protest dictionaries within long term memory
        for influence in ideologies:
            if influence in protest:
                if "Democratic" in influence:
                    self.long_term_memory['Ideologies'][0]['Democratic'] += (
                        protest[influence]['protest occurred'][0]['Influence'])

                elif "Communist" in influence:
                    self.long_term_memory['Ideologies'][0]['Communist'] += (
                        protest[influence]['protest occurred'][0]['Influence'])

                elif "Fascist" in influence:
                    self.long_term_memory['Ideologies'][0]['Fascist'] += (
                        protest[influence]['protest occurred'][0]['Influence'])

                elif "Autocratic" in influence:
                    self.long_term_memory['Ideologies'][0]['Autocratic'] += (
                        protest[influence]['protest occurred'][0]['Influence'])
