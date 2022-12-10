from dsu import dsu

def mst(graph, n):
    edges = []
    DSU = dsu(n)
    for i in range(n):
        for j in range(i+1,n):
          edges.append((graph[i][j]['weight'],i,j))  
    edges.sort()
    value = 0
    adj = [[] for i in range(n)]
    for w,i,j in edges:
        if(DSU.find(i) == DSU.find(j)):
            continue
        adj[i].append(j)
        adj[j].append(i)
        value += w
        DSU.union(i,j)
    return adj