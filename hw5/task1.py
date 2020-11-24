import pandas as pd
import numpy as np


def find_more_than(df):
    n = float(input("Enter the "))
    filter_large = df['Richter'] >= n
    df_sorted = df.loc[filter_large]
    print("Task A\n", df_sorted)
    count = 0
    for i in df_sorted.groupby(['Richter']).size():
        count += 1
    return df_sorted,count


df=pd.read_csv("quake.csv")
# print(df.head(5))
# df_sorted = pd.DataFrame(np.sort(df, axis=0), columns=df.columns)
# print(df_sorted)

df,count = find_more_than(df)
print("Task1\n",df.groupby(['Richter']).size(),'\n',count)
print(df.nlargest(10,'Richter'))

