#!/usr/bin/python

import ast
import inspect
import math
print ("Hello, Python!")

def get_g (L, T, th):
    theta = th * math.pi / 180.0
    par = (1 + 1.0 / 4.0 * math.sin(theta/2)**2)
    return ((4.0 * (math.pi ** 2) * L / T ** 2) * par)

if __name__ == "__main__":
    L=0.5
    T=1.443
    th=30

    g = get_g(0.5, 1.443, 30)
    g1 = get_g(0.5-0.05,1.443+0.02,30-5)
    print("g (0.5,1.443,30) = " + str(g))
    print("g (0.5-0.05,1.443+0.02,30-5) = " + str(g1))
    print("delta(g)/g = " + str((g - g1) / g))
