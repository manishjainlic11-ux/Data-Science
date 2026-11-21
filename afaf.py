import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Penguins Data (2).csv')

plt.figure()
sns.scatterplot(data=df, x = 'Culmen Length (mm)', y = 'Body Mass (g)')
plt.title("Culmen length vs Body mass")
plt.show() 


plt.figure()
sns.scatterplot(data=df, x = 'Culmen Depth (mm)', y ='Body Mass (g)')
plt.title('Culmen Depth vs Body Mass')
plt.show()

sns.pairplot(df)
plt.show()

df[['Culmen Length (mm)','Body Mass (g)']].dropna(),plt.area()
plt.title('Area Graph: Culmen Length and Body Mass')
plt.show()