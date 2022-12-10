from mst import mst
import networkx as nx
class christofides:
    def __init__(self, g, n):
        self.n = n
        self.graph = g
        self.mst = mst(g,n)
    def tsp(self):
        vertices = self.get_odd_vertices()
        adj_odd = [[]]
        for v in vertices:
            adj_odd.append(self.graph[v])
        nx_graph = nx.from_numpy_matrix(adj_odd)

        
    def get_odd_vertices(self):
        odd_vertices = set()
        for row,index in self.mst:
            edges = 0
            for elm in row:
                edges += (elm > 0)
            if edges%2:
                odd_vertices.add(index)
        return list(odd_vertices)