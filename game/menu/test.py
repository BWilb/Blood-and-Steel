"""economic_objectives = ["increase wages for workers", "pass tax breaks for businesses",
                                       "maintain low taxes"]
economic_objectives = ["increase taxes", "increase government spending", "increase exports"]
economic_objectives = ["increase corporate taxes", "increase government spending", "increase income taxes",
                                       ]
economic_objectives = ["increase taxes", "increase government spending", "cut workers wages",
                                       "increase corporate taxes"]"""
# Initialize a dictionary with lists of lists as values
objectives = {
            "objectives": [
                {"foreign objectives": [],
                "domestic": [
                        {
                            'population objectives': [],
                            'economic objectives': [],
                            'political objectives': [],
                            'social objectives': []
                        }
                    ]
                }
            ]
        }
political_objectives = ["repress rival factions", "maintain political growth", "increase political stability"]
objectives['objectives'][0]['domestic'][0]['political objectives'].append(political_objectives)
print(objectives)