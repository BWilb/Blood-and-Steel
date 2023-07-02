from datetime import datetime


class Prussia:
    def __init__(self, year, master_nation):
        self.current_date = datetime(year, 1, 1)
        # administrative variables
        self.name = "Prussia"
        # social variables
        self.current_pop = 0
        # economic variables
        self.government_spending = 0
        self.investment = 0
        self.consumer_spending = 0
        self.exports = 0
        self.imports = 0
        # political variables
        self.stability = 96.65
        self.master = master_nation
