import os
from us_states import (alabama, alaska, arizona, arkansas, california, colorado,
                       conneticut, delaware, florida, georgia, hawaii, idaho, illinois,
                       indiana, iowa, kansas, kentucky, louisiana, maine, maryland, massachuesetts,
                       missouri, michigan, minnesota, mississppi, n_d, n_m, nebraska, nevada,
                       new_hampshire, new_jersey, new_york, north_carolina, ok, oregon, pennsylvania,
                       rhode_island, s_d, south_carolina, tennessee, texas, utah, vermont, virginia,
                       washington, west_virginia, wisconsin, wyoming)

folder = "us_states"

for file in os.listdir(folder):
    if file != '__pycache__':
        print(file.removesuffix(".py"))

states = [alabama, alaska, arizona, arkansas, california, colorado,
                       conneticut, delaware, florida, georgia, hawaii, idaho, illinois,
                       indiana, iowa, kansas, kentucky, louisiana, maine, maryland, massachuesetts,
                       missouri, michigan, minnesota, mississppi, n_d, n_m, nebraska, nevada,
                       new_hampshire, new_jersey, new_york, north_carolina, ok, oregon, pennsylvania,
                       rhode_island, s_d, south_carolina, tennessee, texas, utah, vermont, virginia,
                       washington, west_virginia, wisconsin, wyoming]
for state in states:
    """States variable will contain separate memory storage of state files"""
    for file in os.listdir(folder):
        if state == file:
            print(state)