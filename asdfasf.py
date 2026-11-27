import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Penguins Data (4).csv")

print(df.isnull().sum())

sns.heatmap(df.isnull())
plt.title("Missing Values Heatmap")
plt.show()

num_cols = df.select_dtypes(include="number").columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

cat_cols = df.select_dtypes(include="object").columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print(df.isnull().sum())

sns.pairplot(df)
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

sns.boxplot(data=df)
plt.title("Boxplot of Numerical Features")
plt.xticks(rotation=45)
plt.show()

sns.countplot(x="Gender", data=df)
plt.title("Count of Penguins by Gender")
plt.show()
