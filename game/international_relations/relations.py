def establish_relations(nation1, nation2, nation_network):
    if not nation_network.has_edge(nation1, nation2):
        print('hi')
        nation_network.add_edge(nation1, nation2)