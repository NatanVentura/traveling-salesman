from mst import mst
class twice_around_the_tree:
    def __init__(self,graph,n):
        self.graph = graph
        self.n = n
        self.adj = mst(graph,n)
        self.vis = [False]*self.n
        self.path = []
    def tsp(self):
        self.dfs(0)
        self.path.append(0)
        cost = 0
        for i in range(1,len(self.path)):
            cost += self.graph.get_edge(self.path[i-1],self.path[i])
        return cost
    def dfs(self,i):
        self.vis[i] = True
        self.path.append(i)
        for j in self.adj[i]:
            if self.vis[j]:
                continue
            self.vis[j] = True
            self.dfs(j)

    