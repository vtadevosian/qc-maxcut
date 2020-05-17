import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, n, E, isWeighted = False):
        assert isinstance(n, int), 'n is not an integer: {}'.format(n)
        assert n > 0, 'n is not positive: {}'.format(n)
        self.n = n
        
        edgelist = []
        for edge in E:
            assert isinstance(edge[0], int), 'edge[0] is not an integer: {}'.format(edge[0])
            assert isinstance(edge[1], int), 'edge[1] is not an integer: {}'.format(edge[1])
            assert 0 <= edge[0] < n, 'edge[0] is not in range [0, {}]: {}'.format(edge[0], n-1)
            assert 0 <= edge[1] < n, 'edge[1] is not in range [0, {}]: {}'.format(edge[1], n-1)
            edgelist.append(edge if isWeighted else (edge[0], edge[1], 1.0))
                
        self.E = edgelist
        
        self.V = np.arange(0, n, 1)

        G = nx.Graph()
        G.add_nodes_from(self.V)
        G.add_weighted_edges_from(self.E) # to-do: non-weighted case
            
        self.G = G
        self.isWeighted = isWeighted

    def draw(self, color = 'c', node_size=600, alpha=1, colors=None, cut_edges=None):
        if colors is None:
            colors = [color for node in self.G.nodes()]
        ax = plt.axes(frameon=True)
        pos = nx.spring_layout(self.G)
        
        if self.isWeighted:
            weights = nx.get_edge_attributes(self.G,'weight')
            nx.draw_networkx_edge_labels(self.G,pos,edge_labels=weights)
        nx.draw_networkx(self.G, node_color=colors, node_size=node_size, style='dashed', alpha=alpha,ax=ax, pos=pos)
        
        if cut_edges is not None:
            nx.draw_networkx_edges(self.G, edgelist=cut_edges, style='solid', pos=pos)