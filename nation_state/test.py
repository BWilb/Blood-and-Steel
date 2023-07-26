def stability_happiness_change(self, globe):
    if globe.tension > 25 and globe.tension < 50:
        """if global tension is between 25 and 50"""
        if self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
            if self.improve_stability > self.date:
                """if improving of stability has been activated"""

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability(relationship is not bidirectional)
                    """
                    stability_increase = round(random.uniform(0.25, 1.56), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                    happiness_increase = round(random.uniform(1.56, 2.56), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

                else:
                    happiness_increase = round(random.uniform(1.25, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

            else:
                stability_increase = round(random.uniform(0.15, 1.10), 2)
                if (self.stability + stability_increase) < 100:
                    self.stability += stability_increase

    elif globe.tension > 50 and globe.tension < 75:
        """if global tension is between 50 and 75"""
        if self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
            if self.improve_stability > self.date:
                """if improving of stability has been activated"""

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    stability_increase = round(random.uniform(0.10, 1.25), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                    happiness_increase = round(random.uniform(1.15, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

                else:
                    happiness_increase = round(random.uniform(0.04, 0.96), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

            else:
                happiness_increase = round(random.uniform(1.35, 2.50), 2)
                if (self.happiness + happiness_increase) < 100:
                    self.happiness += happiness_increase

    elif globe.tension > 75:
        """if global tension is above 75"""
        if self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
            if self.improve_stability > self.date:
                """if improving of stability has been activated"""

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    stability_increase = round(random.uniform(0.05, 0.75), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                    happiness_increase = round(random.uniform(0.5, 1.15), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

                else:
                    happiness_decrease = round(random.uniform(1.35, 2.25), 2)
                    if (self.happiness - happiness_decrease) < 100:
                        self.happiness -= happiness_decrease

            else:
                stability_decrease = round(random.uniform(0.05, 0.75), 2)
                if (self.stability - stability_decrease) < 100:
                    self.stability -= stability_decrease
    else:
        print('hi')
        """if global tension is below 25"""
        if self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
            if self.improve_stability > self.date:
                """if improving of stability has been activated"""
                stability_increase = round(random.uniform(0.05, 0.75), 2)
                if (self.stability + stability_increase) < 100:
                    self.stability += stability_increase

            else:
                stability_increase = round(random.uniform(1.05, 2.75), 2)
                if (self.stability + stability_increase) < 100:
                    self.stability += stability_increase

            if self.improve_happiness > self.date:
                """if improving of happiness has been activated
                improved happiness improves stability, if policies have been 
                put into place for improving national happiness(relationship is not bidirectional)
                """
                stability_increase = round(random.uniform(0.05, 0.75), 2)
                if (self.stability + stability_increase) < 100:
                    self.stability += stability_increase

                happiness_increase = round(random.uniform(0.5, 1.15), 2)
                if (self.happiness + happiness_increase) < 100:
                    self.happiness += happiness_increase

            else:
                happiness_increase = round(random.uniform(0.25, 1.56), 2)
                if (self.happiness + happiness_increase) < 100:
                    self.happiness += happiness_increase