import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Penguins Data (1).csv")

features = ["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (g)"]
colors = ["skyblue", "coral", "lightgreen", "gold"]
bins_counts = [20, 15, 25, 12]

for i in range(4):
    plt.figure()
    plt.hist(df[features[i]].dropna(), bins=bins_counts[i], color=colors[i], edgecolor="black")
    plt.title(features[i])
    plt.xlabel(features[i])
    plt.ylabel("Frequency")

plt.show()
