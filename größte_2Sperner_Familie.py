
import numpy as np
import scipy
import itertools

m = 4
menge = {i for i in range(m)}
potenzmenge = [set(c) for r in range(len(menge) + 1)
               for c in itertools.combinations(menge, r)]
l = len(potenzmenge)

A = []
b = []

for B in potenzmenge:
    for C in potenzmenge:
        if B < C:
            for D in potenzmenge:
                    if D > C:
                        row = np.zeros(l)
                        row[potenzmenge.index(B)] = 1
                        row[potenzmenge.index(C)] = 1
                        row[potenzmenge.index(D)] = 1
                        A.append(row)
                        b.append(2)

bounds = [(0, 1)] * l
c = -np.ones(l, dtype=int)

result = scipy.optimize.linprog(c, A, b, bounds=(0,1), integrality=1)
result.x

antichain = []
for i in range(l):
    if result.x[i] == 1:
        antichain.append(potenzmenge[i])
print(antichain)
