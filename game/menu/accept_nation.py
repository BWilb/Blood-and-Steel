import random

from nation_state.north_america.mexico import mexico
from nation_state.north_america.mexico import mexico_ai
from nation_state.north_america.canada import canada
from nation_state.north_america.canada import canada_ai
from nation_state.north_america.cuba import cuba
from nation_state.north_america.cuba import cuba_ai
from nation_state.north_america.united_states import us
from nation_state.north_america.united_states import us_ai
from nation_state.europe.britain import britain_ai
from nation_state.europe.britain import britain
from nation_state.europe.italy import italy_ai
from nation_state.europe.italy import italy
from nation_state.europe.france import france_ai
from nation_state.europe.france import france
from nation_state.europe.belgium import belgium
from nation_state.europe.belgium import belgium_ai
from nation_state.europe.denmark import denmark
from nation_state.europe.denmark import denmark_ai
from nation_state.europe.spain import spain
from nation_state.europe.spain import spain_ai
from nation_state.europe.austria import austria
from nation_state.europe.austria import austria_ai
#from nation_state.europe.luxembourg import luxembourg
from nation_state.europe.luxembourg import luxembourg_ai, luxembourg
from nation_state.europe.netherlands import netherlands
from nation_state.europe.netherlands import netherlands_ai
from nation_state.europe.greece import greece
from nation_state.europe.greece import greece_ai
from nation_state.europe.hungary import hungary
from nation_state.europe.hungary import hungary_ai
from nation_state.europe.sweden import sweden
from nation_state.europe.sweden import sweden_ai
from nation_state.europe.germany import german_ai
from nation_state.europe.germany import germany
from nation_state.europe.romania import romania
from nation_state.europe.romania import romania_ai
from nation_state.europe.norway import norway
from nation_state.europe.norway import norway_ai
from nation_state.europe.lithuania import lithuania
from nation_state.europe.lithuania import lithuania_ai
from nation_state.europe.latvia import latvia
from nation_state.europe.latvia import latvia_ai
from nation_state.europe.latvia import latvia
from nation_state.europe.estonia import estonia
from nation_state.europe.estonia import estonia_ai
from nation_state.europe.russia import russia
from nation_state.europe.russia import russia_ai
from nation_state.europe.switzerland.swiss_ai import SwitzerlandAI
from nation_state.europe.switzerland.swiss import Switzerland
from nation_state.europe.bulgaria import bulgaria_ai
from nation_state.europe.bulgaria import bulgaria
from nation_state.europe.poland import poland
from nation_state.europe.poland import poland_ai
from nation_state.europe.portugal import portugal_ai
from nation_state.europe.portugal import portugal
from nation_state.asia.se_asia.japan import japan
from nation_state.asia.se_asia.japan import japan_ai
from nation_state.asia.se_asia.china import china
from nation_state.asia.se_asia.china import china_ai
from nation_state.asia.middle_east.iran import iran
from nation_state.asia.middle_east.iran import iran_ai
from nation_state.asia.middle_east.turkey import turkey
from nation_state.asia.middle_east.turkey import turkey_ai
from nation_state.asia.middle_east.afghanistan import afghanistan
from nation_state.asia.middle_east.afghanistan import afghanistan_ai
from nation_state.asia.middle_east.iraq import iraq
from nation_state.asia.middle_east.iraq import iraq_ai
from nation_state.south_america.brazil import brazil
from nation_state.south_america.brazil import brazil_ai
from nation_state.south_america.argentina import argentina
from nation_state.south_america.argentina import argentine_ai
from nation_state.south_america.venezuala import venezuala
from nation_state.south_america.venezuala import venezuala_ai
from nation_state.south_america.columbia import columbia
from nation_state.south_america.columbia import columbia_ai
#from nation_state.south_america.venezuala import venezuala
from nation_state.south_america.peru import peru_ai
from nation_state.south_america.peru import peru
#from nation_state.south_america.venezuala import venezuala
from nation_state.south_america.chile import chile_ai
from nation_state.south_america.chile import chile
from nation_state.south_america.bolivia import bolivia_ai
from nation_state.south_america.bolivia import bolivia

def establish_nations(globe, user_nation, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function
    player nation will also be appended to globe's nation list
    """
    for i in range(0, len(args)):

        if args[i].leader is not None and not args[i].is_chosen:
            args[i].establish_map_coordinates()
            args[i].establishing_beginning_objectives()
            args[i].establish_foreign_objectives()
            globe.nations.append(args[i])

    user_nation.establish_map_coordinates()
    globe.nations.append(user_nation)
    for nation in range(0, len(globe.nations)):
        """establishing loop to loop through list of nations"""
        for foreign_nation in range(0, len(globe.nations)):
            if not globe.nations[nation].name == globe.nations[foreign_nation]:
                """Looping through nations that will be foreign to nation variable"""
                relation = random.randrange(0, 100)
                relation_status = ''
                if relation >= 75:
                    relation_status = "ally"

                elif 45 < relation < 75:
                    relation_status = "rival"

                elif relation < 45:
                    relation_status = "enemy"

                globe.nations[nation].foreign_relations['foreign relations'].append({
                    "nation": globe.nations[foreign_nation],
                    "relations": relation,
                    "relation status": relation_status,
                    "guaranteeing independence": False,
                    "alliance": "",
                    "embargoed": False,
                    "war goal": False,
                    "at war with": False
                })

def establish_json_files(time):
    from nation_data.retreive_data import JsonWriter
    json_writer = JsonWriter(int(time))
    json_writer.clear_old_file()


def accept_nation(nation, time):
    #print(time)
    from globe_relations import globe
    from sprite_game_revised import SpriteGame
    #from practice_sprite import SpriteGame
    establish_json_files(time)

    globe1 = globe.Globe(time)

    if nation.lower() == "austria":
        austrian = austria.Austria(globe1)
        austrian.is_chosen = True
        afghan_ai = afghanistan_ai.AfghanistanAI(globe1)
        argentinian_ai = argentine_ai.Argentina(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        english_ai = britain_ai.Britain(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        # chinese_ai = china_ai.ChinaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        germany1 = german_ai.GermanAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        establish_nations(globe1, austrian, afghan_ai, english_ai, dutch_ai, swiss_ai, belgian_ai,
                          french_ai, greek_ai, norwegian_ai, russian_ai, portuguese_ai, bulgarian_ai,
                          polish_ai, spanish_ai, danish_ai, hungarian_ai, luxembourger_ai, swedish_ai, estonian_ai,
                          latvian_ai, lithuanian_ai, canadian_ai, american_ai, mexican_ai, cuban_ai, germany1,
                          brazilian_ai, venezuelan_ai, chilean_ai, bolivian_ai, columbian_ai,
                          peruvian_ai, romanian_ai, turkish_ai, japanese_ai, argentinian_ai, iranian_ai, iraqi_ai, italian_ai)

        game = SpriteGame(austrian, globe1)
        game.main_game()

    if nation.lower() == "afghanistan":
        afghan = afghanistan.Afghanistan(globe1)
        afghan.is_chosen = True
        argentinian_ai = argentine_ai.Argentina(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        austrian_ai = austria_ai.Austria(globe1)
        english_ai = britain_ai.Britain(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        #chinese_ai = china_ai.ChinaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        germany1 = german_ai.GermanAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        establish_nations(globe1, afghan, austrian_ai, english_ai, dutch_ai, swiss_ai, belgian_ai,
                          french_ai, greek_ai, norwegian_ai, russian_ai, portuguese_ai, bulgarian_ai,
                          polish_ai, spanish_ai, danish_ai, hungarian_ai, luxembourger_ai, swedish_ai, estonian_ai,
                          latvian_ai, lithuanian_ai, canadian_ai, american_ai, mexican_ai, cuban_ai, germany1,
                          brazilian_ai, venezuelan_ai, chilean_ai, bolivian_ai, columbian_ai,
                          peruvian_ai, romanian_ai, turkish_ai, japanese_ai, argentinian_ai, iranian_ai, iraqi_ai, italian_ai)

        game = SpriteGame(afghan, globe1)
        game.main_game()

    if nation.lower() == "argentina":
        argentine = argentina.Argentina(globe1)
        argentine.is_chosen = True
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        austrian_ai = austria_ai.Austria(globe1)
        english_ai = britain_ai.Britain(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        #chinese_ai = china_ai.ChinaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        germany1 = german_ai.GermanAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        establish_nations(globe1, argentine, austrian_ai, english_ai, dutch_ai, swiss_ai, belgian_ai,
                          french_ai, greek_ai, norwegian_ai, russian_ai, portuguese_ai, bulgarian_ai,
                          polish_ai, spanish_ai, danish_ai, hungarian_ai, luxembourger_ai, swedish_ai, estonian_ai,
                          latvian_ai, lithuanian_ai, canadian_ai, american_ai, mexican_ai, cuban_ai, germany1,
                          brazilian_ai, venezuelan_ai, chilean_ai, bolivian_ai, columbian_ai,
                          peruvian_ai, romanian_ai, turkish_ai, japanese_ai, afghani_ai, iranian_ai, iraqi_ai, italian_ai)

        game = SpriteGame(argentine, globe1)
        game.main_game()

    if nation.lower() == "belgium":
        belgian = belgium.Belgium(globe1)
        belgian.is_chosen = True
        austrian_ai = austria_ai.Austria(globe1)
        english_ai = britain_ai.Britain(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        #chinese_ai = china_ai.ChinaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        germany1 = german_ai.GermanAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        establish_nations(globe1, belgian, austrian_ai, english_ai, dutch_ai, swiss_ai,
                          french_ai, greek_ai, norwegian_ai, russian_ai, portuguese_ai, bulgarian_ai,
                          polish_ai, spanish_ai, danish_ai, hungarian_ai, luxembourger_ai, swedish_ai, estonian_ai,
                          latvian_ai, lithuanian_ai, canadian_ai, american_ai, mexican_ai, cuban_ai, germany1,
                          brazilian_ai, argentina_ai, venezuelan_ai, chilean_ai, bolivian_ai, columbian_ai,
                          peruvian_ai, romanian_ai, turkish_ai, japanese_ai, afghani_ai, iranian_ai, iraqi_ai, italian_ai)

        game = SpriteGame(belgian, globe1)
        game.main_game()

    if nation.lower() == "bolivia":
        bolivian = bolivia.Bolivia(globe1)
        bolivian.is_chosen = True
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        austrian_ai = austria_ai.Austria(globe1)
        english_ai = britain_ai.Britain(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        #chinese_ai = china_ai.ChinaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        germany1 = german_ai.GermanAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        establish_nations(globe1, bolivian, austrian_ai, english_ai, dutch_ai, swiss_ai, belgian_ai,
                          french_ai, greek_ai, norwegian_ai, russian_ai, portuguese_ai, bulgarian_ai,
                          polish_ai, spanish_ai, danish_ai, hungarian_ai, luxembourger_ai, swedish_ai, estonian_ai,
                          latvian_ai, lithuanian_ai, canadian_ai, american_ai, mexican_ai, cuban_ai, germany1,
                          brazilian_ai, argentina_ai, venezuelan_ai, chilean_ai, columbian_ai,
                          peruvian_ai, romanian_ai, turkish_ai, japanese_ai, afghani_ai, iranian_ai, iraqi_ai, italian_ai)

        game = SpriteGame(bolivian, globe1)
        game.main_game()

    if nation.lower() == "brazil":
        brazilian = brazil.Brazil(globe1)
        brazilian.is_chosen = True
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        austrian_ai = austria_ai.Austria(globe1)
        english_ai = britain_ai.Britain(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        #chinese_ai = china_ai.ChinaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        germany1 = german_ai.GermanAI(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        establish_nations(globe1, brazilian, austrian_ai, english_ai, dutch_ai, swiss_ai, belgian_ai,
                          french_ai, greek_ai, norwegian_ai, russian_ai, portuguese_ai, bulgarian_ai,
                          polish_ai, spanish_ai, danish_ai, hungarian_ai, luxembourger_ai, swedish_ai, estonian_ai,
                          latvian_ai, lithuanian_ai, canadian_ai, american_ai, mexican_ai, cuban_ai, germany1,
                          bolivian_ai, argentina_ai, venezuelan_ai, chilean_ai, columbian_ai,
                          peruvian_ai, romanian_ai, turkish_ai, japanese_ai, afghani_ai, iranian_ai, iraqi_ai, italian_ai)

        game = SpriteGame(brazilian, globe1)
        game.main_game()

    if nation.lower() == "great britain":
        british = britain.Britain(globe1)
        british.is_chosen = True
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, british, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(british, globe1)
        game.main_game()

    if nation.lower() == "bulgaria":
        bulgarian = bulgaria.Bulgaria(globe1)
        bulgarian.is_chosen = True
        british_ai = britain_ai.Britain(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, bulgarian, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          british_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(bulgarian, globe1)
        game.main_game()

    if nation.lower() == "canada":
        canadian = canada.Canada(globe1)
        canadian.is_chosen = True
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, canadian, luxembourger_ai, spanish_ai, bulgarian_ai, russian_ai, belgian_ai,
                          british_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(canadian, globe1)
        game.main_game()

    if nation.lower() == "chile":
        chilean = chile.Chile(globe1)
        chilean.is_chosen = True
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, chilean, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          british_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, bulgarian_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(chilean, globe1)
        game.main_game()

    if nation.lower() == "columbia":
        columbian = columbia.Columbia(globe1)
        columbian.is_chosen = True
        chilean_ai = chile_ai.Chile(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, columbian, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          british_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, bulgarian_ai, venezuelan_ai,
                          chilean_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(columbian, globe1)
        game.main_game()

    if nation.lower() == "cuba":
        cuban = cuba.Cuba(globe1)
        cuban.is_chosen = True
        columbian_ai = columbia_ai.Columbia(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, cuban, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          british_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          columbian_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, bulgarian_ai, venezuelan_ai,
                          chilean_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(cuban, globe1)
        game.main_game()

    if nation.lower() == "denmark":
        danish = denmark.Denmark(globe1)
        danish.is_chosen = True
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, danish, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          british_ai, italian_ai, bulgarian_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(danish, globe1)
        game.main_game()

    if nation.lower() == "estonia":
        estonian = estonia.Estonia(globe1)
        estonian.is_chosen = True
        danish_ai = denmark_ai.Denmark(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, estonian, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          british_ai, italian_ai, bulgarian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,danish_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(estonian, globe1)
        game.main_game()

    if nation.lower() == "france":
        french = france.France(globe1)
        french.is_chosen = True
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, french, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          british_ai, italian_ai, bulgarian_ai, estonian_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai, danish_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(french, globe1)
        game.main_game()

    if nation.lower() == "germany":
        germany1 = germany.Germany(globe1)
        germany1.is_chosen = True
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, germany1, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, luxembourger_ai, estonian_ai, french_ai, danish_ai, greek_ai,
                          hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai,
                          venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(germany1, globe1)
        game.main_game()

    if nation.lower() == "greece":
        greek = greece.Greece(globe1)
        greek.is_chosen = True
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        germany1 = german_ai.GermanAI(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, greek, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, luxembourger_ai, estonian_ai, french_ai, danish_ai, germany1,
                          hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai,
                          venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(greek, globe1)
        game.main_game()

    if nation.lower() == "hungary":
        hungarian = hungary.Hungary(globe1)
        hungarian.is_chosen = True
        greek_ai = greece_ai.Greece(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        germany1 = german_ai.GermanAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, hungarian, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, luxembourger_ai, estonian_ai, french_ai, danish_ai, germany1,
                          greek_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai,
                          venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(hungarian, globe1)
        game.main_game()

    if nation.lower() == "iran":
        iranian = iran.Iran(globe1)
        iranian.is_chosen = True
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        germany1 = german_ai.GermanAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, iranian, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, luxembourger_ai, estonian_ai, french_ai, danish_ai, germany1,
                          greek_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai,
                          venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, hungarian_ai, iraqi_ai)

        game = SpriteGame(iranian, globe1)
        game.main_game()

    if nation.lower() == "iraq":
        iraqi = iraq.Iraq(globe1)
        iraqi.is_chosen = True
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        germany1 = german_ai.GermanAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        establish_nations(globe1, iraqi, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, luxembourger_ai, estonian_ai, french_ai, danish_ai, germany1,
                          greek_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai,
                          venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, hungarian_ai, iranian_ai)

        game = SpriteGame(iraqi, globe1)
        game.main_game()

    if nation.lower() == "italy":
        italian = italy.Italy(globe1)
        italian.is_chosen = True
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, italian, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, british_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(italian, globe1)
        game.main_game()

    if nation.lower() == "japan":
        japanese = japan.Japan(globe1)
        japanese.is_chosen = True
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, japanese, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, british_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, italian_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(japanese, globe1)
        game.main_game()

    if nation.lower() == "luxembourg":
        luxembourger = luxembourg.Luxembourg(globe1)
        luxembourger.is_chosen = True
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, luxembourger, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(luxembourger, globe1)
        game.main_game()

    if nation.lower() == "latvia":
        latvian = latvia.Latvia(globe1)
        latvian.is_chosen = True
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, latvian, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          luxembourger_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(latvian, globe1)
        game.main_game()

    """if nation.lower() == "lithuania":
        lithuanian = lithuania.Lithuania(globe1)
        lithuanian.is_chosen = True
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, lithuanian, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai,
                          luxembourger_ai, latvian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(lithuanian, globe1)
        game.main_game()"""

    if nation.lower() == "mexico":
        mexican = mexico.Mexico(globe1)
        mexican.is_chosen = True
        dutch_ai = netherlands_ai.Netherlands(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, mexican, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai, lithuanian_ai,
                          luxembourger_ai, latvian_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, dutch_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(mexican, globe1)
        game.main_game()

    if nation.lower() == "netherlands":
        dutch = netherlands.Netherlands(globe1)
        dutch.is_chosen = True
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, dutch, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai, lithuanian_ai,
                          luxembourger_ai, latvian_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(dutch, globe1)
        game.main_game()

    if nation.lower() == "norway":
        norwegian = norway.Norway(globe1)
        norwegian.is_chosen = True
        dutch_ai = netherlands_ai.Netherlands(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, norwegian, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai, lithuanian_ai,
                          luxembourger_ai, latvian_ai, dutch_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(norwegian, globe1)
        game.main_game()

    if nation.lower() == "peru":
        peruvian = peru.Peru(globe1)
        peruvian.is_chosen = True
        norwegian_ai = norway_ai.NorwayAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, peruvian, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai, lithuanian_ai,
                          luxembourger_ai, latvian_ai, dutch_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, norwegian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(peruvian, globe1)
        game.main_game()

    if nation.lower() == "poland":
        polish = poland.Poland(globe1)
        polish.is_chosen = True
        norwegian_ai = norway_ai.NorwayAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, polish, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai, norwegian_ai,
                          bulgarian_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai, lithuanian_ai,
                          luxembourger_ai, latvian_ai, dutch_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(polish, globe1)
        game.main_game()

    if nation.lower() == "portugal":
        portuguese = portugal.Portugal(globe1)
        portuguese.is_chosen = True
        polish_ai = poland_ai.PolandAI(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, portuguese, british_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai, norwegian_ai,
                          bulgarian_ai, italian_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai,
                          romanian_ai, lithuanian_ai,
                          luxembourger_ai, latvian_ai, dutch_ai, polish_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(portuguese, globe1)
        game.main_game()

    if nation.lower() == "romania":
        romanian = romania.Romania(globe1)
        romanian.is_chosen = True
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, romanian, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai,
                          bulgarian_ai, british_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai, italian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(romanian, globe1)
        game.main_game()

    if nation.lower() == "russia":
        russian = russia.Russia(globe1)
        russian.is_chosen = True
        romanian_ai = romania_ai.RomaniaAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, russian, luxembourger_ai, spanish_ai, canadian_ai, romanian_ai, belgian_ai,
                          bulgarian_ai, british_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai, italian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(russian, globe1)
        game.main_game()

    if nation.lower() == "spain":
        spanish = spain.Spain(globe1)
        spanish.is_chosen = True
        russian_ai = russia_ai.RussiaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, spanish, luxembourger_ai, russian_ai, canadian_ai, romanian_ai, belgian_ai,
                          bulgarian_ai, british_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai, italian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, swedish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(spanish, globe1)
        game.main_game()

    if nation.lower() == "sweden":
        swedish = sweden.Sweden(globe1)
        swedish.is_chosen = True
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        swiss_ai = SwitzerlandAI(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, swedish, luxembourger_ai, russian_ai, canadian_ai, romanian_ai, belgian_ai,
                          bulgarian_ai, british_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai, italian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, spanish_ai, swiss_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(swedish, globe1)
        game.main_game()

    if nation.lower() == "switzerland":
        swiss = Switzerland(globe1)
        swiss.is_chosen = True
        swedish_ai = sweden_ai.SwedenAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, swiss, luxembourger_ai, russian_ai, canadian_ai, romanian_ai, belgian_ai,
                          bulgarian_ai, british_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai, italian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, spanish_ai, swedish_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(swiss, globe1)
        game.main_game()

    if nation.lower() == "turkey":
        turkish = turkey.Turkey(globe1)
        turkish.is_chosen = True
        swiss_ai = SwitzerlandAI(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, turkish, luxembourger_ai, russian_ai, canadian_ai, romanian_ai, belgian_ai,
                          bulgarian_ai, british_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai, italian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, spanish_ai, swedish_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, swiss_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(turkish, globe1)
        game.main_game()

    if nation.lower() == "united states":
        american = us.US(globe1)
        american.is_chosen = True
        swiss_ai = SwitzerlandAI(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, american, luxembourger_ai, russian_ai, canadian_ai, romanian_ai, belgian_ai,
                          bulgarian_ai, british_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai, italian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, spanish_ai, swedish_ai,
                          cuban_ai, mexican_ai, swiss_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, venezuelan_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(american, globe1)
        game.main_game()

    if nation.lower() == "venezuela":
        venezuelan = venezuala.Venezuala(globe1)
        venezuelan.is_chosen = True
        swiss_ai = SwitzerlandAI(globe1)
        swedish_ai = sweden_ai.SwedenAI(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        bulgarian_ai = bulgaria_ai.BulgariaAI(globe1)
        british_ai = britain_ai.Britain(globe1)
        danish_ai = denmark_ai.Denmark(globe1)
        estonian_ai = estonia_ai.EstoniaAI(globe1)
        french_ai = france_ai.FranceAI(globe1)
        germany1 = german_ai.GermanAI(globe1)
        greek_ai = greece_ai.Greece(globe1)
        hungarian_ai = hungary_ai.HungaryAI(globe1)
        italian_ai = italy_ai.ItalyAI(globe1)
        latvian_ai = latvia_ai.LatviaAI(globe1)
        lithuanian_ai = lithuania_ai.LithuaniaAI(globe1)
        dutch_ai = netherlands_ai.Netherlands(globe1)
        norwegian_ai = norway_ai.NorwayAI(globe1)
        polish_ai = poland_ai.PolandAI(globe1)
        portuguese_ai = portugal_ai.Portugal(globe1)
        cuban_ai = cuba_ai.CubaAI(globe1)
        mexican_ai = mexico_ai.MexicoAI(globe1)
        american_ai = us_ai.USAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, venezuelan, luxembourger_ai, russian_ai, canadian_ai, romanian_ai, belgian_ai,
                          bulgarian_ai, british_ai, danish_ai, estonian_ai, french_ai, germany1, greek_ai, hungarian_ai, italian_ai,
                          latvian_ai, lithuanian_ai, dutch_ai, norwegian_ai, polish_ai, portuguese_ai, spanish_ai, swedish_ai,
                          cuban_ai, mexican_ai, american_ai, argentina_ai, bolivian_ai, brazilian_ai, chilean_ai, swiss_ai,
                          columbian_ai, peruvian_ai, afghani_ai, turkish_ai, japanese_ai, iranian_ai, iraqi_ai)

        game = SpriteGame(venezuelan, globe1)
        game.main_game()