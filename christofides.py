from mst import mst
import networkx as nx
class christofides:
    def __init__(self, g, n):
        self.n = n
        self.graph = g
        self.mst = mst(g,n)
        self.answer = 0
    def tsp(self):
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
        print(matching)
        print(self.mst)
        for i,row in enumerate(self.mst):
            for j in row:
                if(i < j):
                    continue
                euler_multigraph.add_edge(i,j,weight = self.graph[i][j]['weight'])
        for edge in matching:
            euler_multigraph.add_edge(edge[0], edge[1],
                                    weight=self.graph[edge[0]][edge[1]]['weight'])
        print(euler_multigraph.edges)
        euler_tour = list(nx.eulerian_circuit(euler_multigraph, source=0))
        path = []
        nds = set()
        for elm in euler_tour:
            if elm[0] not in nds:
                nds.add(elm[0])
                path.append(elm[0])
        path.append(0)
        print(path)
        for i in range(len(path)-1):
            self.answer += self.graph[path[i]][path[i+1]]['weight']
        #print(self.answer)

        
    def get_odd_vertices(self):
        odd_vertices = set()
        for index,row in enumerate(self.mst):
            if len(row)%2:
                odd_vertices.add(index)
        return odd_vertices