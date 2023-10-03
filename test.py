import networkx as nx
import matplotlib.pyplot as plt

class YourGraphClass:
    def __init__(self):
        # Create an empty graph when the class is instantiated
        self.network = nx.Graph()

    def establish_relations(self, nation1, nation2):
        if not self.network.has_edge(nation1, nation2):
            print('Adding edge between', nation1, 'and', nation2)
            self.network.add_edge(nation1, nation2)
            # You can choose to display the graph here if needed
        else:
            print("Edge already exists between", nation1, 'and', nation2)
    def draw(self):
        nx.draw(self.network, with_labels=True)

# Example usage:
your_graph = YourGraphClass()
your_graph.establish_relations('NationA', 'NationB')
your_graph.establish_relations('NationA', 'NationB')  # This will print "Edge already exists..."
your_graph.draw()
plt.show()
