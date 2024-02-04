import pandas as pd


df1 = pd.read_csv("shared_articles.csv")
df2 = pd.read_csv("users_interactions.csv")

print(df1.head(5))
print(df2.head(5))

