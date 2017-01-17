
from graph import Lab_Graph
from sdj import UnionFind
import time

Zero = Lab_Graph(20,30)
A_start = time.time()
Zero.AldousBroderGenerate()
A_stop = time.time()
B =A_stop - A_start

print Zero, A_stop - A_start
A_start = time.time()
Zero.PrimGenerate()
A_stop = time.time()
C = A_stop - A_start
print Zero, A_stop - A_start

A_start = time.time()
Zero.KruskallGenerate()
A_stop = time.time()
D = A_stop - A_start
print Zero, A_stop - A_start

print B,C,D

# Statystyka Od Najwolniejszego : Aldous, Prim , Kruskal 

