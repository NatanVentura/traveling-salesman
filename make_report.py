import time
import generator
from branch_and_bound import bnb
from christofides import christofides
from twice_around_the_tree import twice_around_the_tree

def report(alg_type, dist_type, i):
    N = 2**i
    g = generator.gen(N,7,type=dist_type)
    file_name = alg_type + '_'+ dist_type +'_' + str(i)  + '.txt'
    inicio = time.time()
    if alg_type == 'branch_and_bound':
        algorithm = bnb(g,N)
    elif alg_type == 'christofides':
        algorithm = christofides(g,N)
    elif alg_type == 'twice_and_around_the_tree':
        algorithm = twice_around_the_tree(g,N)
    algorithm.tsp()
    tempo_total = time.time() - inicio
    f = open('./results/reports.csv', "a")
    f.write(str(N)+','+alg_type + ','+dist_type + ',' +"{:.2f}".format(algorithm.answer) + "," + "{:.2f}".format(tempo_total)+'\n')
    f.close()

