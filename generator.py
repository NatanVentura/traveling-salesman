from random import *
from math import sqrt
import networkx as nx

MAX = int(1000)

def e_dist(p1,p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def m_dist(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def gen(n,s = 7):
    #seed(s)
    e_graph = nx.Graph()
    m_graph = nx.Graph()
    for i in range(n):
        e_graph.add_node(i)
        m_graph.add_node(i)
    v = []
    for i in range(n):
        v.append((randint(0,MAX),randint(0,MAX)))
    #print(v)
    for i in range(0,n):
        for j in range(i+1,n):
            #print('i',i,'j',j,"e_dist:",e_dist(v[i],v[j]))
            e_graph.add_edge(i,j, weight = e_dist(v[i],v[j]))
            m_graph.add_edge(i,j,weight = m_dist(v[i],v[j]))
        #print()
    return (e_graph,m_graph)

MAT = [[9999,    64,  378, 519, 434, 200], 
[64,  9999,    318, 455, 375, 164] ,
[378 ,318 ,9999    ,170 ,265, 344 ],
[519 ,455, 170, 9999,    223, 428 ],
[434 ,375 ,265, 223, 9999,    273 ],
[200, 164, 344, 428, 273, 9999]]

def getGraph():
    n = len(MAT)
    g = nx.Graph()
    for i in range(n):
        g.add_node(i)
    for i in range(n):
        for j in range(i+1,n):
            g.add_weighted_edges_from([(i,j,MAT[i][j])])
    return g