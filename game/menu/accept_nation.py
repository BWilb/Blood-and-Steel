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

def establish_foreign_nations(globe, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function"""
    for i in range(0, len(args)):
        if args[i].leader is not None:
            globe.nations.append(args[i])
def accept_nation(nation, time):
    print(time)
    from globe_relations import globe
    from sprite_game_revised import SpriteGame

    globe1 = globe.Globe(time)
    if nation.lower() == "mexico":
        mexican = mexico.Mexico(globe1)
        canadian = canada_ai.Canada(globe1)
        cuban = cuba_ai.CubaAI(globe1)
        british = britain_ai.Britain(globe1)
        italian = italy_ai.ItalyAI(globe1)
        french = france_ai.FranceAI(globe1)
        danish = denmark_ai.Denmark(globe1)
        spanish = spain_ai.SpainAI(globe1)
        greek = greece_ai.Greece(globe1)
        dutch = netherlands_ai.Netherlands(globe1)
        austrian = austria_ai.Austria(globe1)
        luxembourger = luxembourg_ai.LuxembourgAI(globe1)
        belgian = belgium_ai.BelgiumAI(globe1)
        swedish = sweden_ai.SwedenAI(globe1)
        romanian = romania_ai.RomaniaAI(globe1)
        norwegian = norway_ai.NorwayAI(globe1)
        russian = russia_ai.RussiaAI(globe1)
        polish = poland_ai.PolandAI(globe1)
        japanese = japan_ai.JapanAI(globe1)
        chinese = china_ai.ChinaAI(globe1)
        iranian = iran_ai.Iran(globe1)
        turkish = turkey_ai.TurkeyAI(globe1)
        afghan = afghanistan_ai.AfghanistanAI(globe1)
        iraqi = iraq_ai.Iraq(globe1)

        establish_foreign_nations(globe1, swedish, romanian, british, french, russian, polish, japanese, chinese, iranian, iraqi,
                                  turkish, afghan, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  cuban, mexican, canadian, italian, norwegian)
        game = SpriteGame(mexican, globe1)
        game.main_game()

    if nation.lower() == "austria":
        mexican = mexico_ai.MexicoAI(globe1)
        canadian = canada_ai.Canada(globe1)
        cuban = cuba_ai.CubaAI(globe1)
        british = britain_ai.Britain(globe1)
        italian = italy_ai.ItalyAI(globe1)
        french = france_ai.FranceAI(globe1)
        danish = denmark_ai.Denmark(globe1)
        spanish = spain_ai.SpainAI(globe1)
        greek = greece_ai.Greece(globe1)
        dutch = netherlands_ai.Netherlands(globe1)
        austrian = austria.Austria(globe1)
        luxembourger = luxembourg_ai.LuxembourgAI(globe1)
        belgian = belgium_ai.BelgiumAI(globe1)
        swedish = sweden_ai.SwedenAI(globe1)
        romanian = romania_ai.RomaniaAI(globe1)
        norwegian = norway_ai.NorwayAI(globe1)
        russian = russia_ai.RussiaAI(globe1)
        polish = poland_ai.PolandAI(globe1)
        japanese = japan_ai.JapanAI(globe1)
        chinese = china_ai.ChinaAI(globe1)
        iranian = iran_ai.Iran(globe1)
        turkish = turkey_ai.TurkeyAI(globe1)
        afghan = afghanistan_ai.AfghanistanAI(globe1)
        iraqi = iraq_ai.Iraq(globe1)

        establish_foreign_nations(globe1, swedish, romanian, british, french, russian, polish, japanese, chinese, iranian, iraqi,
                                  turkish, afghan, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  cuban, mexican, canadian, italian, norwegian)
        game = SpriteGame(austrian, globe1)
        game.main_game()


