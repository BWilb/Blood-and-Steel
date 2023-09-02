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
from nation_state.south_america.brazil import brazil_ai
from nation_state.south_america.argentina import argentina
#from nation_state.south_america.argentina import argentina_ai

def establish_foreign_nations(globe, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function"""
    for i in range(0, len(args)):
        if args[i].population != 0 or args[i].current_gdp != 0:
            globe.nations.append(args[i])
def accept_nation(nation, time):
    print(time)
    import globe
    from sprite_game_revised import SpriteGame

    globe1 = globe.Globe()
    if nation.lower() == "mexico":
        mexican = mexico.Mexico(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  cuban, mexican, canadian)
        game = SpriteGame(mexican, globe1)
        game.main_game()


    if nation.lower() == "canada":
        canadian = canada.Canada(time)
        american = us_ai.UnitedStates(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        mexican = mexico_ai.MexicoAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, american, canadian)
        game = SpriteGame(canadian, globe1)
        game.main_game()


        #sprite_version.country_sprite(canadian, globe1)

    if nation.lower() == "cuba":
        cuban = cuba.Cuba(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)
        game = SpriteGame(cuban, globe1)
        game.main_game()

    if nation.lower() == "great britain":
        british = britain.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)

        game = SpriteGame(british, globe1)
        game.main_game()

    if nation.lower() == "italy":
        italian = italy.Italy(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)

        game = SpriteGame(italian, globe1)
        game.main_game()

    if nation.lower() == "france":
        french = france.France(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        belgian = belgium_ai.BelgiumAI(time)
        italian = italy_ai.ItalyAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)

        game = SpriteGame(french, globe1)
        game.main_game()

    if nation.lower() == "belgium":
        belgian = belgium.Belgium(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)

        game = SpriteGame(belgian, globe1)
        game.main_game()

    if nation.lower() == "denmark":
        danish = denmark.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)

        game = SpriteGame(danish, globe1)
        game.main_game()

    if nation.lower() == "spain":
        spanish = spain.Spain(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        danish = denmark_ai.Denmark(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)

        game = SpriteGame(spanish, globe1)
        game.main_game()

    if nation.lower() == "luxembourg":
        luxembourger = luxembourg.Luxembourg(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        spanish = spain_ai.SpainAI(time)
        danish = denmark_ai.Denmark(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)

        game = SpriteGame(luxembourger, globe1)
        game.main_game()

    if nation.lower() == "netherlands":
        dutch = netherlands.Netherlands(time)
        greek = greece_ai.Greece(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        austrian = austria_ai.Austria(time)
        spanish = spain_ai.SpainAI(time)
        danish = denmark_ai.Denmark(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)

        game = SpriteGame(dutch, globe1)
        game.main_game()

    if nation.lower() == "greece":
        greek = greece.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        austrian = austria_ai.Austria(time)
        spanish = spain_ai.SpainAI(time)
        danish = denmark_ai.Denmark(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        establish_foreign_nations(globe1, greek, dutch, luxembourger, austrian, spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian, norwegian, romanian, swedish)

        game = SpriteGame(greek, globe1)
        game.main_game()

    if nation.lower() == "sweden":
        swedish = sweden.Sweden(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, swedish, greek, dutch, luxembourger, austrian, spanish, danish, belgian,
                                  french,
                                  italian, british, cuban, mexican, canadian)

        game = SpriteGame(swedish, globe1)
        game.main_game()

    if nation.lower() == "romania":
        romanian = romania.Romania(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        norwegian = norway_ai.NorwayAI(time)
        establish_foreign_nations(globe1, romanian, swedish, greek, dutch, luxembourger, austrian, spanish, danish,
                                  belgian, french,
                                  italian, norwegian, british, cuban, mexican, canadian)

        game = SpriteGame(romanian, globe1)
        game.main_game()

    if nation.lower() == "norway":
        norwegian = norway.Norway(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        austrian = austria_ai.Austria(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, norwegian, romanian, swedish, greek, dutch, luxembourger, austrian, spanish,
                                  danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)
        game = SpriteGame(norwegian, globe1)
        game.main_game()

    if nation.lower() == "austria":
        austrian = austria.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, austrian, norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french,
                                  italian, british, cuban, mexican, canadian)
        game = SpriteGame(austrian, globe1)
        game.main_game()

    if nation.lower() == "russia":
        russian = russia.Russia(time)
        austrian = austria_ai.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, russian, austrian, norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french, italian, british, cuban, mexican, canadian)

        game = SpriteGame(russian, globe1)
        game.main_game()

    if nation.lower() == "poland":
        polish = poland.Poland(time)
        russian = russia_ai.RussiaAI(time)
        austrian = austria_ai.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, polish, austrian, norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french, russian, italian, british, cuban, mexican, canadian)
        game = SpriteGame(polish, globe1)
        game.main_game()

    if nation.lower() == "japan":
        japanese = japan.Japan(time)
        chinese = china_ai.ChinaAI(time)
        polish = poland_ai.PolandAI(time)
        russian = russia_ai.RussiaAI(time)
        austrian = austria_ai.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, japanese, chinese, polish, austrian, norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french, russian, italian, british, cuban, mexican, canadian)
        game = SpriteGame(japanese, globe1)
        game.main_game()

    if nation.lower() == "china":
        chinese = china.China(time)
        japanese = japan_ai.Japan(time)
        #polish = poland_ai.PolandAI(time)
        russian = russia_ai.RussiaAI(time)
        austrian = austria_ai.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, chinese, japanese, austrian, norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french, russian, italian, british, cuban, mexican, canadian)
        game = SpriteGame(chinese, globe1)
        game.main_game()

    if nation.lower() == "iran":
        iranian = iran.Iran(time)
        chinese = china_ai.ChinaAI(time)
        japanese = japan_ai.Japan(time)
        polish = poland_ai.PolandAI(time)
        russian = russia_ai.RussiaAI(time)
        austrian = austria_ai.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, iranian, chinese, japanese, polish, austrian, norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french, russian, italian, british, cuban, mexican, canadian)
        game = SpriteGame(iranian, globe1)
        game.main_game()

    if nation.lower() == "turkey":
        turkish = turkey.Turkey(time)
        iranian = iran_ai.Iran(time)
        chinese = china_ai.ChinaAI(time)
        japanese = japan_ai.Japan(time)
        polish = poland_ai.PolandAI(time)
        russian = russia_ai.RussiaAI(time)
        austrian = austria_ai.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, turkish, iranian, chinese, japanese, polish, austrian, norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french, russian, italian, british, cuban, mexican, canadian)
        game = SpriteGame(turkish, globe1)
        game.main_game()

    if nation.lower() == "afghanistan":
        afghan = afghanistan.Afghanistan(time)
        turkish = turkey_ai.TurkeyAI(time)
        iranian = iran_ai.Iran(time)
        chinese = china_ai.ChinaAI(time)
        japanese = japan_ai.Japan(time)
        polish = poland_ai.PolandAI(time)
        russian = russia_ai.RussiaAI(time)
        austrian = austria_ai.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, afghan, turkish, iranian, chinese, japanese, polish, austrian, norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french, russian, italian, british, cuban, mexican, canadian)
        game = SpriteGame(afghan, globe1)
        game.main_game()

    if nation.lower() == "iraq":
        iraqi = iraq.Iraq(time)
        afghan = afghanistan_ai.AfghanistanAI(time)
        turkish = turkey_ai.TurkeyAI(time)
        iranian = iran_ai.Iran(time)
        chinese = china_ai.ChinaAI(time)
        japanese = japan_ai.Japan(time)
        polish = poland_ai.PolandAI(time)
        russian = russia_ai.RussiaAI(time)
        austrian = austria_ai.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, iraqi, afghan, turkish, iranian, chinese, japanese, polish, austrian,
                                  norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french, russian, italian, british, cuban, mexican, canadian)
        game = SpriteGame(iraqi, globe1)
        game.main_game()

    if nation.lower() == "brazil":
        brazilian = brazil.Brazil(time)
        iraqi = iraq_ai.Iraq(time)
        afghan = afghanistan_ai.AfghanistanAI(time)
        turkish = turkey_ai.TurkeyAI(time)
        iranian = iran_ai.Iran(time)
        chinese = china_ai.ChinaAI(time)
        japanese = japan_ai.Japan(time)
        polish = poland_ai.PolandAI(time)
        russian = russia_ai.RussiaAI(time)
        austrian = austria_ai.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, brazilian, iraqi, afghan, turkish, iranian, chinese, japanese, polish, austrian,
                                  norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french, russian, italian, british, cuban, mexican, canadian)
        game = SpriteGame(brazilian, globe1)
        game.main_game()

    if nation.lower() == "argentina":
        argentine = argentina.Argentina(time)
        #brazilian = brazil.Brazil(time)
        iraqi = iraq_ai.Iraq(time)
        afghan = afghanistan_ai.AfghanistanAI(time)
        turkish = turkey_ai.TurkeyAI(time)
        iranian = iran_ai.Iran(time)
        chinese = china_ai.ChinaAI(time)
        japanese = japan_ai.Japan(time)
        polish = poland_ai.PolandAI(time)
        russian = russia_ai.RussiaAI(time)
        austrian = austria_ai.Austria(time)
        norwegian = norway_ai.NorwayAI(time)
        romanian = romania_ai.RomaniaAI(time)
        swedish = sweden_ai.SwedenAI(time)
        mexican = mexico_ai.MexicoAI(time)
        canadian = canada_ai.Canada(time)
        cuban = cuba_ai.CubaAI(time)
        british = britain_ai.Britain(time)
        italian = italy_ai.ItalyAI(time)
        french = france_ai.FranceAI(time)
        danish = denmark_ai.Denmark(time)
        spanish = spain_ai.SpainAI(time)
        greek = greece_ai.Greece(time)
        dutch = netherlands_ai.Netherlands(time)
        luxembourger = luxembourg_ai.LuxembourgAI(time)
        belgian = belgium_ai.BelgiumAI(time)
        establish_foreign_nations(globe1, argentine, iraqi, afghan, turkish, iranian, chinese, japanese, polish, austrian,
                                  norwegian, romanian, swedish, greek, dutch, luxembourger,
                                  spanish, danish, belgian, french, russian, italian, british, cuban, mexican, canadian)
        game = SpriteGame(argentine, globe1)
        game.main_game()