"""import keyboard

if keyboard.read_key("Space"):
    print("end")"""
import time

"""File is meant for experimentation"""
from datetime import timedelta, datetime
import math

date = datetime(int("1936"), 1, 1)

for i in range(0, 10000):
    date += timedelta(days=1)
    if (date.year % 4 == 0 and date.month == 11 and date.day == 7):
        print(date)


print(math.pow(2, 10000) )

"""self.democratic_supporters = self.population * 0.85
            self.republican_supporters = (self.population - self.democratic_supporters) * 0.75
            self.communist_supporters = (self.population - (
                        self.democratic_supporters + self.republican_supporters)) * 0.3
            self.socialist_supporters = (self.population - (self.democratic_supporters + self.republican_supporters +
                                                            self.communist_supporters)) * 0.2
            self.nationalist_supporters = (self.population - (self.democratic_supporters + self.republican_supporters +
                                                              .communist_supporters + .socialist_supporters)) * 0.5
            .non_alligned = (.population - (us.democratic_supporters + us.republican_supporters +
                                                    us.communist_supporters + us.socialist_supporters +
                                                    us.nationalist_supporters))
"""



from nation_state.europe.germany.germany import *

