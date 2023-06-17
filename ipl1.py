import pandas as pd
import matplotlib.pyplot as plt
import random
df = pd.read_csv(r'C:/Users/akhar/OneDrive/Desktop/IPL - Player Performance Dataset/IPL/IPL_Ball_by_Ball_2008_2022.csv' ,  encoding = 'latin1')
print(df.head())
print(df.info())
new_df = df[df['ID']==1312200]
length = 233
first = new_df[new_df['innings']==1]
length = 120
first['balls'] = [(i % length) + 1 for i in range(length)]
first['runs'] = first['total_run'].cumsum()
print(first)
second = new_df[new_df['innings']==2]
length1 = 113
second['balls'] = [(i % length1) + 1 for i in range(length1)]
second['runs'] = second['total_run'].cumsum()
print(second)
x = first['balls']
y = first['runs']
x1 = second['balls']
y2 = second['runs']
legends = ['rajasthan' , 'gujarat']
plt.plot(x,y , "-b" , label = legends[0])
plt.plot(x1,y2, "-r" , label = legends[1])
plt.legend()
plt.xlabel("balls")
plt.ylabel("runs")
plt.title("RR vs GT")
plt.show()
