import pandas as pd
import numpy as np


quake=pd.read_csv("quake.csv")
print("Task 1a\n")
quake1 = quake.nlargest(10,'Richter')
print(quake1)
print('Task 1b')
quake2=quake.nlargest(10,'Focal depth')
print(quake2)
print('Task 1c')
north_quake=quake[quake['Latitude']>0]
north_west_quake=north_quake[north_quake['Latitude']<0]
print(north_quake['Focal depth'],north_west_quake)

air_quality = pd.read_csv("AirQualityUCI.csv")
print(air_quality.drop(['Date','Time'],axis=1))



