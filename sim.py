from __future__ import division, print_function
import numpy as np
from pylab import *

P = np.random.poisson
L = linspace(0,20,1000)
X = P(L, size=(10000,len(L)))

P = dict((k, sum(X==k,axis=0)/sum(X==k)) for k in range(4))

print("Expected value of L for a given observed k")
for k,Pi in sorted(P.items()):
    print(k, sum(L*Pi))

print("Variance of L for a given observed k")
for k, Pi in sorted(P.items()):
    print(k, sum((L-(k+1))**2*Pi))

for k,Pi in sorted(P.items()):
    plot(L, Pi/(L[1]-L[0]), label="k=%d"%k, hold=True)
xlabel(r'$\lambda$')
ylabel(r'$P(\lambda|k)$')
xticks([0,1,2,3,4,5,6,7,8,9,10])
axis([0, 10, 0, 0.5])
title('Probability of underlying rate $\lambda$ for different observed $k$')
legend()
grid(True)
show()


