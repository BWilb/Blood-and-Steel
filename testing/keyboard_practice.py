"""import keyboard

if keyboard.read_key("Esc"):
    print("end")"""

"""File is meant for experimentation"""
from datetime import timedelta, datetime

date = datetime(int("1939"), 1, 1)

for i in range(0, 40):
    print(date + timedelta(days=i))
    print(date.year)

from nation_state.europe.germany.germany import *