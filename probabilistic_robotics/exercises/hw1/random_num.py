#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# use seed() to generate same 'random' variables
np.random.seed(9001)
'''
Create a vector with 100000 random variables which are normally distributed
with a mean of 5.0 and a standard deviation of 2.0.
'''
sig = 2
mu = 5
ran_var = sig * np.random.randn(100000, 1)+mu
#print(ran_var)
#ran_var = np.transpose(ran_var)
#print(ran_var)
'''
Create a vector with 100000 uniformly distributed random variables between
0 and 10.
'''
uni_var = np.random.uniform(0,10,100000)
#print(uni_var)

ave_ran = np.sum(ran_var)/100000
ave_uni = np.sum(uni_var)/100000

print(ave_ran)
print(ave_uni)
'''
plt.hist(ran_var)
plt.show()
plt.hist(uni_var)
plt.show()
'''
