from queue import PriorityQueue

class graph:
    def __init__(self,n):
        self.adj = [[0 for x in range(n)] for y in range(n)] 
        self.edge_list = [[] for y in range(n)] 
        self.sorted_edges = [[] for y in range(n)] 
    def add_edge(self,i,j,w):
        self.adj[i][j] = w
        self.adj[j][i] = w
        self.sorted_edges[j].append((w,i))
        self.sorted_edges[i].append((w,j))
    def get_edge(self,i,j):
        return self.adj[i][j]
    def get_sorted_edges(self,i):
        self.sorted_edges[i].sort()
        return self.sorted_edges[i]