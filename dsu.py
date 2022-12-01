class dsu:
    def __init__(self,n):
        self.parent = []
        for i in range(n):
            self.parent.append(i)
        self.size = [1]*n
    def union(self,i,j):
        parent1 = self.find(i)
        parent2 = self.find(j)
        if(parent1 == parent2):
            return
        if(parent1 < parent2):
            parent1,parent2 = parent2, parent1
        self.size[parent1] += parent2
        self.parent[parent2] = parent1
    def find(self,i):
        if(self.parent[i] == i):
            return i
        return self.find(self.parent[i])
    
    