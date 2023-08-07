from datetime import datetime, timedelta

first_date = datetime(1914, 1, 1)
duration = timedelta(weeks=30)

for day in range(duration.days):
    for hour in range(1, 25):
        dday = first_date + timedelta(hours=hour)
        print(dday)
    first_date += timedelta(days=1)
    first_date.