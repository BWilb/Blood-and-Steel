from nation_state.north_america.mexico import mexico
from nation_state.north_america.mexico import mexico_ai
from nation_state.north_america.canada import canada
from nation_state.north_america.canada import canada_ai
from nation_state.north_america.cuba import cuba
from nation_state.north_america.cuba import cuba_ai
#from nation_state.north_america.united_states import us
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
from nation_state.europe.luxembourg import luxembourg
from nation_state.europe.luxembourg import luxembourg_ai
from nation_state.europe.netherlands import netherlands
from nation_state.europe.netherlands import netherlands_ai
from nation_state.europe.greece import greece
from nation_state.europe.greece import greece_ai
from nation_state.europe.sweden import sweden
from nation_state.europe.sweden import sweden_ai
from nation_state.europe.romania import romania
from nation_state.europe.romania import romania_ai
from nation_state.europe.norway import norway
from nation_state.europe.norway import norway_ai
from nation_state.europe.russia import russia
from nation_state.europe.russia import russia_ai
from nation_state.europe.poland import poland
from nation_state.europe.poland import poland_ai
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
from nation_state.south_america.argentina import argentina
#from nation_state.south_america.argentina import argentina_ai

def establish_nations(globe, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function
    player nation will also be appended to globe's nation list
    """
    for i in range(0, len(args)):
        if args[i].leader is not None:
            globe.nations.append(args[i])
def accept_nation(nation, time):
    print(time)
    from globe_relations import globe
    from sprite_game_revised import SpriteGame

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

    if nation.lower() == "romania":
        romanian = romania.Romania(globe1)
        """luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        belgian_ai = belgium_ai.BelgiumAI(globe1)
        austrian_ai = austria_ai.Austria(globe1)"""
        establish_nations(globe1, romanian)
        game = SpriteGame(romanian, globe1)
        game.main_game()

    if nation.lower() == "belgium":
        belgian = belgium.Belgium(globe1)
        luxembourger_ai = luxembourg_ai.LuxembourgAI(globe1)
        romanian_ai = romania_ai.RomaniaAI(globe1)
        austrian_ai = austria_ai.Austria(globe1)
        iraqi_ai = iraq_ai.Iraq(globe1)
        establish_nations(globe1, belgian, austrian_ai, romanian_ai, luxembourger_ai, iraqi_ai)
        game = SpriteGame(belgian, globe1)
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
