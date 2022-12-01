from branch_and_bound import bnb
from generator import gen,getGraph
from graph import graph
from twice_around_the_tree import twice_around_the_tree

p = 32
g1,g2 = gen(p,10)
g3 = getGraph()
a = bnb(g1,p)
#a = bnb(g3,6)


#MAT = [29 ,20, 21, 16 ,31 ,100 ,12 ,4 ,31 ,18,15 ,29 ,28 ,40 ,72 ,21 ,29 ,41 ,12,15 ,14 ,25 ,81 ,9 ,23 ,27 ,13,4 ,12 ,92 ,12 ,25 ,13 ,25,16 ,94 ,9 ,20 ,16 ,22,95 ,24 ,36 ,3, 37,90 ,101 ,99 ,84,15 ,25,13,35,18,38]
with open('mat.txt', 'r') as f:
    MAT = [[int(num) for num in line.rstrip().split(' ')] for line in f]
n = len(MAT)
print(MAT)
g4 = graph(n)
k = 0
for i in range(n):
    for j in range(i+1,n):
        g4.add_edge(i,j,MAT[i][j])
        k += 1

b = twice_around_the_tree(g4,n)
a = bnb(g4,n)
b.tsp()
#a.tsp()
print(a.answer)
#print("a:",a.path)
print("b:",b.tsp())
""" def printBin(x):
    if(x == 0):
        print()
        return
    printBin(x//2)
    print(x&1,end='') """

""" msk = bit_mask(10)
printBin(msk.mask)
msk.put(5)
msk.put(2)
printBin(msk.mask)
printBin(msk.mask)
msk.remove(5)
printBin(msk.mask) """
