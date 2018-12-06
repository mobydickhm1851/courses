#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt


scan = np.loadtxt("./hw2/laserscan.dat")

def give_coordinate(scan_ls, scan_range):
    # set angle to scan point in scan_ls
    angle = np.linspace(-scan_range/2, scan_range/2, np.shape(scan_ls)[0], endpoint = True)
    x_cor, y_cor = [], []     # list for x-y coordinate
    print(angle) 
    for i in range(len(scan_ls)):
        x_cor.append( scan_ls[i]*np.cos(angle[i]))
        y_cor.append( scan_ls[i]*np.sin(angle[i]))
    
    return x_cor, y_cor

plt_x = give_coordinate(scan, math.pi)[0]
plt_y = give_coordinate(scan, math.pi)[1]

fig, ax = plt.subplots()
ax.scatter(plt_x, plt_y, c = 'red', s = 50, label = 'red',alpha = 0.3, edgecolors = 'none')
ax.scatter(0,0, c = 'blue', s = 100, label = 'ROBOT(sensor)', alpha = 0.5)
ax.legend()
ax.grid(True)

plt.show()



