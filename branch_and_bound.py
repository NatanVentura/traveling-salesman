from graph import graph
import bit_mask
from math import ceil
from queue import PriorityQueue

def printBin(x, b = True):
    if(x == 0):
        if(b):
            print(0)
        return
    printBin(x//2,False)
    print(x&1,end='')
    if b:
        print()


class bnb:
    def __init__(self,g, n):
        self.n = n
        self.g = g
        self.answer = float('inf')
        self.min_weights = [[float('inf'),float('inf')] for y in range(self.n)]
        self.selected_edges = [[0,0] for y in range(self.n)]
    def initial_bound(self):
        sum = 0
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    continue
                self.min_weights[i][1] = min(self.min_weights[i][1],self.g.get_edge(i,j))
                if(self.min_weights[i][0] > self.min_weights[i][1]):
                    self.min_weights[i][0],self.min_weights[i][1] = self.min_weights[i][1],self.min_weights[i][0]
            sum += (self.min_weights[i][0]+self.min_weights[i][1])
        return ceil(sum/2)
    
    def tsp(self, mask=0,node=0, deep = 0, cur_bound = 0, cur_weight = 0):
        if(deep == 0):
            cur_bound = self.initial_bound()
        if(deep == self.n-1):
            cur_weight += self.g.get_edge(node,0)
            self.answer = min(self.answer, cur_weight)
            return
        
        for i in range(self.n):
            w = self.g.get_edge(i,node)
            if(bit_mask.has(mask,i)):
                continue
            if(i == node or i == 0):
                continue
            cur_weight += w
            next_bound = cur_bound
            if (deep==1):
                next_bound -= (self.min_weights[node][0] + self.min_weights[i][0])//2
            else:
                next_bound -= (self.min_weights[node][1] + self.min_weights[i][0])//2
            if(next_bound + cur_weight < self.answer):
                mask = bit_mask.put(mask,i)
                self.tsp(mask,i,deep+1,next_bound,cur_weight)
                mask = bit_mask.remove(mask,i)