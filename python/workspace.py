import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

style.use('ggplot')

df = pd.read_csv(r"C:\Users\shado\Desktop\Facharbeit\python\data\AAPL.csv", parse_dates=True, index_col=0)
#df.reset_index(inplace=True)
print(type(df['close']))
print(len(df['close']))
print('____________________________')
temp = 0
for price in df['close']:
    temp += price

expected = temp / len(df['close'])
print('Expected Value:')
print(expected)
