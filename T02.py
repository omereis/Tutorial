#!/usr/bin/python


print ("Hello, Python!, This is T02")

import matplotlib.pyplot as plt
import numpy as np
import mpld3

fig, ax = plt.subplots()
np.random.seed(0)
x, y = np.random.normal(size=(2, 200))
color, size = np.random.random((2, 200))

ax.scatter(x, y, c=color, s=500 * size, alpha=0.3)
ax.grid(color='lightgray', alpha=0.7)
