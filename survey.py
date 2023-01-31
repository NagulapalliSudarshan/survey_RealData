import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# dataset as a numpy array
energy_consumption=np.array([130,55,45,64,155,66,60,80,102,62,\
58,101,75,111,151,139,81,55,66,90,\
97,77,51,67,125,50,136,55,83,91,\
54,86,100,78,93,113,111,104,96,113,\
96,87,129,109,69,94,99,97,83,97])
print(type(energy_consumption))

# creating a dataframe
rates=["40-49","50-59","60-69","70-79","80-89","90-99","100-109","110-119",\
      "120-129","130-139","140-149","150-159"]
df=pd.DataFrame({"Rates":rates,"LowerBound":np.arange(40,151,10),"UpperBound":np.arange(49,160,10)})

# appending frequency into the dataframe
df["Frequency"]=np.arange(12);
for i in range(12):
  count=0
  for _ in energy_consumption:
    if df.loc[i,"LowerBound"]<=_<=df.loc[i,"UpperBound"]:
      count+=1;
  df.loc[i,"Frequency"]=count

# appending relative frequency into the dataframe
df["RelativeFrequency"]=np.arange(12);
relativeFrequency=df.loc[:,"Frequency"].copy()
for i in range(12):
  relativeFrequency[i]/=50
  df.loc[i,"RelativeFrequency"]=relativeFrequency[i]

# printing the dataframe
df.to_csv("Energy_Consumption.csv")
print(df)
print(df.sum(axis=0))

# plotting the line graph
plt.style.use("dark_background")
plt.plot(df["Rates"],df["RelativeFrequency"],color="cyan",marker="o",label="relative Frequecy")
plt.grid(True)
plt.legend()
plt.xlabel("Rates")
plt.ylabel("Frequencies")
plt.title("Energy Consumption in India")
plt.show()