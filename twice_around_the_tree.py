from mst import mst
import time
class twice_around_the_tree:
    def __init__(self,graph,n):
        self.graph = graph
        self.n = n
        self.adj = []
        self.vis = [False]*self.n
        self.path = []
        self.answer = 0
    def tsp(self):
        self.adj = mst(self.graph,self.n)
        self.dfs(0)
        self.path.append(0)
        for i in range(1,len(self.path)):
            self.answer += self.graph[self.path[i-1]][self.path[i]]["weight"]
    def dfs(self,i):
        self.vis[i] = True
        self.path.append(i)
        for j in self.adj[i]:
            if self.vis[j]:
                continue
            self.vis[j] = True
            self.dfs(j)

    