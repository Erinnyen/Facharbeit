import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

# graph with dimensions 7.50 x 4.50
plt.rcParams["figure.figsize"] = [7.50, 4.50]
plt.rcParams["figure.autolayout"] = True

def f(x):
    return np.sin(x)


def N(x, mu, sigma):
    return np.exp(-np.square(x-mu/sigma)/2)/(np.sqrt(2*np.pi*sigma))


mu = 0.2
sigma = 1
x_space = 5
# x interval +- x_space times the variance around the mean
x = np.linspace(mu - x_space*sigma, mu + x_space*sigma, 100)

plt.plot(x, N(x, mu, sigma), color='red')


# makes the grid visible
plt.grid()
# shows the graph
plt.show()
