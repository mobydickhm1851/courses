#!/usr/bin/env python
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt 

def someMath(x):
    return np.cos(x)*np.exp(x)

x_plt = np.arange(-2*pi, 2*pi, 0.2)
y_plt = someMath(x_plt)

plt.plot(x_plt, y_plt)
plt.show()

'''
num = int(input("give me an x"))
print(someMath(num))
'''