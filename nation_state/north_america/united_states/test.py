import os
from nation_state.north_america.united_states.us_states import alaska, arkansas, delaware, alabama, conneticut, \
    california, arizona, colorado, iowa

folder = "us_states"

for file in os.listdir(folder):
    if file != '__pycache__':
        pass
        #print(file.removesuffix(".py"))

states = [alabama, alaska, arizona, arkansas, california, colorado,
          conneticut, delaware, iowa]
us_states = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado",
                       "conneticut", "delaware", "iowa"]
state = us_states[0]
for state in states:
    for file in os.listdir(folder):
        pass