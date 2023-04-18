from datetime import *
year = 1865
date = datetime(year, 1, 1)
cur_date = date

for i in range(365):
    date = date + timedelta(days=1)
    if cur_date.year < date.year:
        print(date)

