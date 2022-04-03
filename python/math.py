import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

# graph with dimensions 7.50 x 4.50
plt.rcParams["figure.figsize"] = [7.50, 4.50]
plt.rcParams["figure.autolayout"] = True

def f(x):
    return np.sin(x)


def N(x, mu, sigma):
    return np.exp((np.square(x-mu)/np.square(sigma))/-2) /(np.sqrt(2*np.pi)* sigma)


mu = 0.2
sigma = 1
x_space = 5
# x interval +- x_space times the variance around the mean
x = np.linspace(-5, 5, 1000)

#plt.plot(x, N(x, mu, sigma), color='red')

plt.plot(x, N(x, 1, 1), "-r", label=('μ: ' + str(1) + ', σ: '+ str(1)))
plt.legend(loc="upper left")

plt.plot(x, N(x, 0, 1), "-b", label=('μ: ' + str(0) + ', σ: '+ str(1)))
plt.legend(loc="upper left")

plt.plot(x, N(x, 0, 2), "-g", label=('μ: ' + str(0) + ', σ: '+ str(2)))
plt.legend(loc="upper left")

plt.plot(x, N(x, 0, 0.8), color='purple', label=('μ: ' + str(0) + ', σ: '+ str(0.8)))
plt.legend(loc="upper left")

plt.plot(x, N(x, -1, 0.5), color='orange', label=('μ: ' + str(-1) + ', σ: '+ str(0.5)))
plt.legend(loc="upper left")

# makes the grid visible
plt.grid()
# shows the graph
plt.show()
