import pandas as pd

data = pd.read_csv("data/titanic.csv")

print(data.isnull().sum())
print(data.shape)

data.dropna(inplace=True)
print(data.isnull().sum())
print(data.shape)

################## NOTES ########################

# We can apply dropna() function to total dataset but can't
# apply to a single column
