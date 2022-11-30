from branch_and_bound import bnb
from generator import gen,getGraph
p = 32
g1,g2 = gen(p,10)
g3 = getGraph()
a = bnb(g1,p)
#a = bnb(g3,6)
a.tsp()
print(a.answer)

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
