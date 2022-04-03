import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import numpy as np
from scipy import stats


#style.use('ggplot')

# graph with dimensions 7.50 x 4.50
plt.rcParams["figure.figsize"] = [10, 6]
plt.rcParams["figure.autolayout"] = True

df = pd.read_csv(r"C:\Users\shado\Desktop\Facharbeit\python\data\sp500-monthly-1870.csv", parse_dates=True, index_col=0)
#df.reset_index(inplace=True)

def N(x, mu, sigma):
    return np.exp((np.square(x-mu)/np.square(sigma))/-2) /(np.sqrt(2*np.pi)* sigma)

# function to add a return column to the dataset/sigma
def renditen():
    # new empty column in the pandas dataframe
    df['renditen'] = pd.NaT

    for x in range(0, len(df['SP500'])):
        if x != 0:
            r = df['SP500'][x] / df['SP500'][x - 1] - 1
            df.loc[df.index[x], 'renditen'] = np.round(r, 2)
        else:
            rowIndex = df.index[x]
            df.loc[rowIndex, 'renditen'] = 0
    df['renditen'] = df['renditen'].astype(np.float64)




# function for expected value in discrete dataset
def mean(column):
    return df[column].sum() / len(df[column])

def stdev(column):
    s = mean(column)
    sum = np.sum(np.square(df[column] - s))
    return np.sqrt(sum / len(df[column]))




returns = df['SP500'].pct_change() # + 1
df.insert(1, 'renditen', returns)

def normaldist():
    mu = mean('renditen')
    sigma = stdev('renditen')
    print('μ(expected):' + str(mu) + '\nσ(standard deviation): '+ str(sigma))

    r_hist = plt.hist(df['renditen'], bins=200, density=True, stacked=True)


    x_space = 10
    # x interval +- x_space times the variance around the mean
    x = np.linspace(mu - x_space*sigma, mu + x_space*sigma, 1000)

    #plt.plot(x, stats.norm.pdf(x, mu, sigma))
    plt.plot(x, N(x, mu, sigma), "-r", label=('Normalverteilung \n'
    + 'μ: ' + str(np.round(mu, 3)) + '\nσ: '+ str(np.round(sigma, 3))))
    plt.legend(loc="upper left")


    print(df['renditen'][(df['renditen'] < -0.2)])

    print(N(-0.25, mu, sigma))

    plt.xlabel('Monatliche Renditen')
    plt.ylabel('Wahrscheinlichkeit in %')
    plt.grid()
    #plt.scatter(df[index])
    plt.show()



normaldist()
