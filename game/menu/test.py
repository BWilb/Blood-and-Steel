"""economic_objectives = ["increase wages for workers", "pass tax breaks for businesses",
                                       "maintain low taxes"]
economic_objectives = ["increase taxes", "increase government spending", "increase exports"]
economic_objectives = ["increase corporate taxes", "increase government spending", "increase income taxes",
                                       ]
economic_objectives = ["increase taxes", "increase government spending", "cut workers wages",
                                       "increase corporate taxes"]"""
options = ["Increase income taxes", "Increase worker wages"]
                option = options[random.randrange(0, len(options))]
                for action in range(0, len(self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'])):
                    # looping through past actions within long term memory
                    for potential_options in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action]["Action Taken"]:
                        # looping through actions taken from past action
                        if (option == potential_options and
                                (self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action]["Timestamps"][-1] +
                                 timedelta(months=3) == date)):
                            # checking
                            # 1. random option equals that of the past option
                            # 2. the timestamp of the past action is 3 months earlier then current action

                            for actions in range(0, len(self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'])):
                                # doing another search through the long term memory of economic decisions
                                if "Continued Recovery" in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][actions]:
                                    # searching for if continued recovery in past action
                                    self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action]["Timestamps"].append(date)
                                else:
                                    # if continued recovery not in past action
                                    self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                                        {"Continued Recovery": [
                                            {"Action Taken": option},
                                            {"Time stamps": [date]}
                                        ]})

                        else:
                            # if original two constraints did not match
                            self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                                {"Continued Recovery": [
                                    {"Action Taken": option},
                                    {"Time stamps": [date]}
                                ]})