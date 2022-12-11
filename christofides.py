from mst import mst
import networkx as nx
class christofides:
    def __init__(self, g, n):
        self.n = n
        self.graph = g
        self.mst = []
        self.answer = 0
        self.path = []
    def tsp(self):
        self.mst = mst(self.graph,self.n)
        odd_graph = nx.Graph()
        odd_vertices = self.get_odd_vertices()
        for i in range(self.n):
            if i not in odd_vertices:
                continue
            for j in range(i+1,self.n):
                if j not in odd_vertices:
                    continue
                odd_graph.add_edge(i,j,weight = self.graph[i][j]['weight'])
        odd_vertices = list(odd_vertices)
        matching = nx.min_weight_matching(odd_graph,maxcardinality=True)
        euler_multigraph = nx.MultiGraph()
        for i,row in enumerate(self.mst):
            for j in row:
                if(i < j):
                    continue
                euler_multigraph.add_edge(i,j,weight = self.graph[i][j]['weight'])
        for edge in matching:
            euler_multigraph.add_edge(edge[0], edge[1],
                                    weight=self.graph[edge[0]][edge[1]]['weight'])
        euler_tour = list(nx.eulerian_circuit(euler_multigraph, source=0))
        nds = set()
        for elm in euler_tour:
            if elm[0] not in nds:
                nds.add(elm[0])
                self.path.append(elm[0])
        self.path.append(0)
        for i in range(len(self.path)-1):
            self.answer += self.graph[self.path[i]][self.path[i+1]]['weight']
        

        
    def get_odd_vertices(self):
        odd_vertices = set()
        for index,row in enumerate(self.mst):
            if len(row)%2:
                odd_vertices.add(index)
        return odd_vertices