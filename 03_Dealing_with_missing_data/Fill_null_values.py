import pandas as pd

data = pd.read_csv("data/titanic.csv")
print(data)
print(data.isnull().sum())

# Filling null values with value 'C85'
data["Cabin"].fillna("C85", inplace=True)
print(data["Cabin"])

##########################################################

data1 = pd.read_csv("data/titanic.csv")
# Filling null values with a value what existed in previous row
data1["Cabin"].fillna(method = 'pad', inplace=True)
print(data1["Cabin"])

##########################################################

data2 = pd.read_csv("data/titanic.csv")
# Filling null values with a value what existed in previous row
data2["Cabin"].fillna(method = 'bfill', inplace=True)
print(data2["Cabin"])
