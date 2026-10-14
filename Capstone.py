import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\MANISH JAIN\OneDrive\Documents\Codingal\After class projects\Capstone\IMDB Dataset.csv")

print(df.head(3))
print(df.tail(3))

df.info()

print(df.isnull().sum())

subset = df.iloc[41:76]
print(subset)

print(df.loc[df["No_of_Votes"].idxmax()])

df["Runtime"] = df["Runtime"].astype(str).str.extract(r"(\d+)").astype(float)

df[["IMDB_Rating", "Runtime"]].boxplot()
plt.show()

plt.scatter(df["IMDB_Rating"], df["Runtime"])
plt.xlabel("IMDB_Rating")
plt.ylabel("Runtime")
plt.show()

sns.histplot(df["IMDB_Rating"], kde=True)
plt.show()
sns.histplot(df["Runtime"], kde=True)
plt.show()

sns.countplot(data=df, x="Certificate")
plt.show()

