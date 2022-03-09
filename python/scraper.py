import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import os


style.use('ggplot')
start = dt.datetime(1980, 1, 1)
end = dt.datetime.now()

API_KEY = 'api/api_key.txt'
with open(API_KEY) as f:
    os.environ['ALPHAVANTAGE_API_KEY'] = f.readlines()[0]

df = web.DataReader("AAPL", "av-monthly", start, end,
                    api_key=os.getenv('ALPHAVANTAGE_API_KEY'))


print(df.head())
# date column has index "index"
# df.reset_index(inplace=True)

df.to_csv('python\data\AAPL.csv')

df['close'].plot()
plt.show()
