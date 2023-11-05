from nation_state.north_america.mexico import mexico
from nation_state.north_america.mexico import mexico_ai
from nation_state.north_america.canada import canada
from nation_state.north_america.canada import canada_ai
from nation_state.north_america.cuba import cuba
from nation_state.north_america.cuba import cuba_ai
# from nation_state.north_america.united_states import us
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
from nation_state.europe.luxembourg import luxembourg_ai
from nation_state.europe.netherlands import netherlands
from nation_state.europe.netherlands import netherlands_ai
from nation_state.europe.greece import greece
from nation_state.europe.greece import greece_ai
from nation_state.europe.hungary import hungary
from nation_state.europe.hungary import hungary_ai
from nation_state.europe.sweden import sweden
from nation_state.europe.sweden import sweden_ai
from nation_state.europe.germany import german_ai
from nation_state.europe.romania import romania
from nation_state.europe.romania import romania_ai
from nation_state.europe.norway import norway
from nation_state.europe.norway import norway_ai
from nation_state.europe.lithuania import lithuania
from nation_state.europe.lithuania import lithuania_ai
from nation_state.europe.latvia import latvia
from nation_state.europe.latvia import latvia_ai
from nation_state.europe.estonia import estonia
from nation_state.europe.estonia import estonia_ai
from nation_state.europe.russia import russia
from nation_state.europe.russia import russia_ai
from nation_state.europe.switzerland.swiss_ai import SwitzerlandAI
from nation_state.europe.bulgaria import bulgaria_ai
from nation_state.europe.poland import poland
from nation_state.europe.poland import poland_ai
from nation_state.europe.portugal import portugal_ai
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
#from nation_state.south_america.columbia import columbia
from nation_state.south_america.columbia import columbia_ai
#from nation_state.south_america.venezuala import venezuala
from nation_state.south_america.peru import peru_ai
#from nation_state.south_america.venezuala import venezuala
from nation_state.south_america.chile import chile_ai
from nation_state.south_america.bolivia import bolivia_ai

def establish_nations(globe, user_nation, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function
    player nation will also be appended to globe's nation list
    """
    for i in range(0, len(args)):
        if args[i].name != user_nation:
            args[i].establishing_beginning_objectives()
            args[i].establish_foreign_objectives()

        if args[i].leader is not None:
            args[i].establish_map_coordinates()
            globe.nations.append(args[i])

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
    """if nation.lower() == "mexico":
        mexican = mexico.Mexico(globe1)

        establish_foreign_nations(globe1, mexican)
        game = SpriteGame(mexican, globe1)
        game.main_game()"""

    if nation.lower() == "austria":
        austrian = austria.Austria(globe1)

        establish_nations(globe1, austrian)
        game = SpriteGame(austrian, globe1)
        game.main_game()

    if nation.lower() == "belgium":
        belgian = belgium.Belgium(globe1)
        belgian.chosen = True
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
        chinese_ai = china_ai.ChinaAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        turkish_ai = turkey_ai.TurkeyAI(globe1)
        japanese_ai = japan_ai.JapanAI(globe1)
        afghani_ai = afghanistan_ai.AfghanistanAI(globe1)
        iranian_ai = iran_ai.Iran(globe1)
        germany = german_ai.GermanAI(globe1)
        brazilian_ai = brazil_ai.Brazil(globe1)
        argentina_ai = argentine_ai.Argentina(globe1)
        venezuelan_ai = venezuala_ai.Venezuala(globe1)
        chilean_ai = chile_ai.Chile(globe1)
        bolivian_ai = bolivia_ai.BoliviaAI(globe1)
        columbian_ai = columbia_ai.Columbia(globe1)
        peruvian_ai = peru_ai.Peru(globe1)
        establish_nations(globe1, belgian, english_ai, austrian_ai, luxembourger_ai, russian_ai, germany, dutch_ai, turkish_ai,
                          iranian_ai, afghani_ai, french_ai, swiss_ai, polish_ai, american_ai, mexican_ai, cuban_ai, japanese_ai,
                          greek_ai, spanish_ai, romanian_ai, italian_ai, danish_ai, norwegian_ai, brazilian_ai, argentina_ai,
                          venezuelan_ai, columbian_ai, chilean_ai, peruvian_ai, iraqi_ai, hungarian_ai, estonian_ai, lithuanian_ai,
                          latvian_ai, canadian_ai, portuguese_ai, swedish_ai, bolivian_ai, bulgarian_ai)
        game = SpriteGame(belgian, globe1)
        game.main_game()

    if nation.lower() == "italy":
        italian = italy.Italy(globe1)
        establish_nations(globe1, italian)
        game = SpriteGame(italian, globe1)
        game.main_game()

    if nation.lower() == "romania":
        romanian = romania.Romania(globe1)
        spanish_ai = spain_ai.SpainAI(globe1)
        russian_ai = russia_ai.RussiaAI(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        canadian_ai = canada_ai.Canada(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        establish_nations(globe1, romanian.name, romanian, luxembourger_ai, spanish_ai, canadian_ai, russian_ai, belgian_ai)
        game = SpriteGame(romanian, globe1)
        game.main_game()

    """if nation.lower() == "luxembourg":
        luxembourger = luxembourg.Luxembourg(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        austrian_ai = austria_ai.Austria(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        establish_nations(globe1, luxembourger, belgian_ai, austrian_ai, romanian_ai)
        game = SpriteGame(luxembourger, globe1)
        game.main_game()

    if nation.lower() == "iraq":
        iraqi = iraq.Iraq(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        austrian_ai = austria_ai.Austria(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        establish_nations(globe1, luxembourger_ai, belgian_ai, austrian_ai, romanian_ai)
        game = SpriteGame(iraqi, globe1)
        game.main_game()"""
