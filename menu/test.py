import random
import time
from datetime import timedelta


def economic_state(us):
    if us.date >= us.economic_change_date:
        """comparing current date with possible shift in business cycle, based upon 3 month cycle"""
        if us.past_gdp > us.current_gdp:
            """comparing past gdp to current gdp"""
            if us.economic_state == "expansion" or us.economic_state == "recovery":
                """current state is expansion or recovery"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recession":
                        print("Your economy has entered into a recession after 6 months of decayed growth.\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=240)
                        """increasing amount of time to check up on GDP
                        Time is average amount(5 months cycle)
                        """

            elif us.economic_state == "recession":
                """current state is recession and cycle is switching to depression"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "depression":
                        print("Your economy has entered into a depression after exceeding 6 months of decayed growth.\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=210)
                        # economic_stimulus(us)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """

        elif us.past_gdp < us.current_gdp:
            if us.economic_state == "depression" or us.economic_state == "recession":
                """current state is expansion or recovery"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recovery":
                        print("Your economy has finally entered its recovery period.\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=360)
                        """increasing amount of time to check up on GDP
                        Time is average amount(5 months cycle)
                        """

            elif us.economic_state == "recovery":
                """current state is recession and cycle is switching to depression"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "expansion":
                        print("Your economy has finally entered its expansionary period. Woo!!!\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=120)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """
