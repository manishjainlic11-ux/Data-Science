from matplotlib import pyplot as plt 
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
#example graphs
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])

fig, ax = plt.subplots(figsize = (10,7))
ax.hist(a, bins = [0,25,50,75,100])

plt.show()


np.random.seed(23685752)
N_points = 10000
n_bins = 20


x = np.random.randn(N_points)
y= .8 ** x + np.random.randn(10000) + 25

fig, axs = plt.subplots(1, 1, figsize = (10, 7), tight_layout = True)
axs.hist(x, bins = n_bins)

plt.show()


# main activity
blood_sugar_men = [113, 85, 90 , 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

type = [blood_sugar_men, blood_sugar_women]
colors = ['g', 'r']
label = ['men', 'women']
bins = [80, 100, 125, 150]
plt.xlabel("Blood Sugar Range")
plt.ylabel("Total no. of patients")

plt.hist(type, bins=bins, rwidth=0.95, color = colors, label=label, orientation="horizontal")

plt.title("Blood Sugar Level Chart")
plt.legend()
plt.show()