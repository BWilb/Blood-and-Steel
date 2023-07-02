import datetime


class Poland:
    def __init__(self, year):
        # Time Variables
        """average variables"""
        self.date = datetime.datetime(int(year), 1, 1)
        self.past_year = self.date.year
        """economic time variables"""
        self.economic_change_date = self.date + timedelta(days=60)
        self.debt_repayment = self.date
        """political time variables"""
        self.political_census = self.date + timedelta(days=3)
        self.improve_stability = self.date
        """social time variables"""
        self.improve_happiness = self.date
        """Stats time variable"""
        self.check_stats = self.date + timedelta(days=3)
        # Political Variables
        # Economic Variables
        # Social Variables
        """average social variables(population)"""
        self.current_pop = population[year]
        self.past_pop = self.current_pop
        self.births = 0
        self.deaths = 0
        self.pop_change = 0
