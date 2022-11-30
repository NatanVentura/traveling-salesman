from queue import PriorityQueue

class graph:
    def __init__(self,n):
        self.adj = [[0 for x in range(n)] for y in range(n)] 
        self.edge_list = [[] for y in range(n)] 
    def add_edge(self,i,j,w):
        self.adj[i][j] = w
        self.adj[j][i] = w
    def get_edge(self,i,j):
        return self.adj[i][j]