import igraph as ig
from random import *
from math import sqrt
import matplotlib.pyplot as plt

MAX = int(1e3)

def e_dist(p1,p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def m_dist(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def gen(n):
    v = []
    for i in range(n):
        v.append((randint(0,MAX),randint(0,MAX)))
    print(v)
    e_edges = []
    m_edges = []
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            e_edges.append((i,j,e_dist(v[i-1],v[j-1])))
            m_edges.append((i,j,m_dist(v[i-1],v[j-1])))
    print(e_edges)
    print(m_edges)
    e_graph = ig.Graph.TupleList(e_edges, weights=True)
    m_graph = ig.Graph.TupleList(m_edges, weights=True)
    return (e_graph,m_graph)



layout = a.layout("kk")
ig.plot(a, layout=layout)
print(a,b)
