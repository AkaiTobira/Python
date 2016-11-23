
from graph import Lab_Graph
import time

Zero = Lab_Graph(60,39)
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

# Statystyka Najwolniejszy : PRIM 1 , Kryskal 85%Prim , Aldos 15%PRIM
