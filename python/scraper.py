import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import os


style.use('ggplot')
start = dt.datetime(1980, 1, 1)
end = dt.datetime.now()

os.environ['ALPHAVANTAGE_API_KEY'] = 'RLO3464TEX2XJYM8'


df = web.DataReader("AAPL", "av-monthly", start, end,
                    api_key=os.getenv('ALPHAVANTAGE_API_KEY'))


print(df.head())
# date column has index "index"
# df.reset_index(inplace=True)

df.to_csv('python\data\AAPL.csv')

df['close'].plot()
plt.show()
