from unicodedata import numeric

import matplotlib.pyplot as plt

x1 = [89, 43, 36, 36,  95, 10, 66 , 34 , 38, 20]

y1 = [21, 46, 3 , 35, 67, 95, 53, 72, 58, 10]

x2 = [26, 29, 48, 64, 6, 5, 36, 66, 72, 40]

y2 = [26, 34, 90, 33, 38, 20, 56, 2, 47, 15]



plt.scatter (x1, y1, c = "pink", linewidths = 2, marker = 's', edgecolor = 'green', s = 50)

plt.scatter(x2, y2, c = 'yellow', linewidths = 2, marker = '^', edgecolor = 'red', s = 200)

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()

import seaborn
import matplotlib.pyplot as plt

df = seaborn.load_dataset('tips')

seaborn.pairplot(df, hue = 'sex')
plt.show()

df = seaborn.pairplot(df, hue = 'day')
plt.show()


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


HouseDF = pd.read_csv("USA_Housing.csv")


HouseDF.head()

HouseDF.info()

HouseDF.describe()



HouseDF.columns

sns.pairplot(HouseDF)

plt.figure(figsize=(8,6))
numeric_df = HouseDF.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot= True, cmap = 'coolwarm', linewidths=0.5)

plt.title("Correlation Heatmap")
plt.show()





