import numpy as np
import matplotlib.pyplot as plt

# e) fix random seed
np.random.seed(123)

# a) normal distribution
mu, sigma = 5.0, 2.0
normal_vector = np.random.normal(mu, sigma, 100000)

# b) uniform distribution
uniform_vector = np.random.uniform(0, 10, 100000)

# c) print mean and std. dev.
print np.mean(normal_vector), np.std(normal_vector)
print np.mean(uniform_vector), np.std(uniform_vector)

# d) plot
plt.figure()
count, bins, ignored = plt.hist(uniform_vector, 100, normed=True)
plt.plot(bins, np.ones_like(bins)*0.1, linewidth=2, color='r')

plt.figure()
count, bins, ignored = plt.hist(normal_vector, 100, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')

plt.show()
