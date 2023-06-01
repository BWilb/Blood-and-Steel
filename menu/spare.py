def politics_change(britain):
    chance = random.randrange(0, 3)
    print(chance)
    if chance == 0:
        """Chance that labour party loses popularity"""
        loss = round(britain.lp * round(random.uniform(0.001, 0.09), 2), 0)
        chance = random.randrange(0, 2)
        if chance == 0:
            """Chance that the CLUP gains in popularity"""
            britain.clup += loss

        elif chance == 1:
            """Chance that the liberal party gains in popularity"""
            britain.liberal += loss

    elif chance == 1:
        """Chance that liberal party loses popularity"""
        loss = round(britain.liberal * round(random.uniform(0.001, 0.09), 2), 0)
        print(loss)
        chance = random.randrange(0, 2)
        if chance == 0:
            """Chance that the CLUP gains in popularity"""
            britain.clup += loss

        elif chance == 1:
            """Chance that the labour party gains in popularity"""
            britain.lp += loss

    elif chance == 2:
        """Chance that the CLUP party loses popularity"""
        loss = round(britain.clup * round(random.uniform(0.001, 0.09), 2), 0)
        print(loss)
        chance = random.randrange(0, 2)
        if chance == 0:
            """Chance that the liberal party gains in popularity"""
            britain.liberal += loss

        elif chance == 1:
            """Chance that the labour party gains in popularity"""
            britain.lp += loss