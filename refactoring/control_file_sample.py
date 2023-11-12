import random
from datetime import timedelta


def democratic_handling_protest(self, political_issue):
    # function handles how democracies approach protests of different ideologies
    days = random.randrange(10, 30)
    if (self.national_policy["Policy"][0]["Domestic Policy"][2][
        "Political stability"] > self.long_term_memory["Domestic Decisions"][0]["Political Decisions"][1][
        'Current stability']):
        for objective in range(0, len(self.objectives[0]["domestic objectives"])):
            """iterating through current objectives"""
            for past_objective in range(0, len(
                    self.long_term_memory['Domestic decisions'][0]["Political Decisions"][0]['protest']
                    [3]['Current political objective'])):
                """iterating through objectives within past decisions"""
                if (self.objectives[0]["domestic objectives"][objective] ==
                        self.long_term_memory['Domestic decisions'][0]["Political Decisions"][0]['protest']
                        [3]['Current political objective'][past_objective]):
                    """Checking if current objective matches with past objective"""
                    if political_issue.values() == "Fascist protest":
                        """Checking if fascist protest"""
                        if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Right"]:
                            """Checking if nation is still suppressing far right"""
                            self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Right protests"][0]["Dates"][1][
                                "End date"] += timedelta(days=days)

                        else:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Right"] = True
                            self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Right protests"].append(
                                {"Dates": [
                                    {"Start date": self.date},
                                    {"End date": self.date + timedelta(days=days)}
                                ]})

                    elif political_issue.values() == "Communist protest":
                        """Checking if far left protest"""
                        if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Left"]:
                            """Checking if nation is still suppressing far left"""
                            self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Left protests"][0]["Dates"][1][
                                "End date"] += timedelta(days=days)

                        else:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Left"] = True
                            self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Left protests"].append(
                                {"Dates": [
                                    {"Start date": self.date},
                                    {"End date": self.date + timedelta(days=days)}
                                ]})

                    elif political_issue.values() == "Autocratic protest":
                        """Checking if autocrat protest"""
                        if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"]:
                            """Checking if nation is still suppressing far left"""
                            self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"][0]["Dates"][1][
                                "End date"] += timedelta(days=days)

                        else:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"] = True
                            self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"].append(
                                {"Dates": [
                                    {"Start date": self.date},
                                    {"End date": self.date + timedelta(days=days)}
                                ]})

                else:
                    if "Arrest dissidents" in self.objectives["objectives"][0]['domestic objectives']:
                        pass
                    elif "Eliminate dissidents" in self.objectives["objectives"][0]['domestic objectives']:
                        pass