import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

style.use('ggplot')

df = pd.read_csv(r"C:\Users\shado\Desktop\Facharbeit\python\data\AAPL.csv", parse_dates=True, index_col=0)
#df.reset_index(inplace=True)
df2 = df.sort_values(by=['close'])
df2.reset_index(inplace=True)
print(df2)
df['close'].plot()
plt.show()



for line in df:
    print(line)
