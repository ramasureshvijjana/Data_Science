import pandas as pd

# Loading Data
data = pd.read_csv("data/titanic.csv")
# Finding Number of null values in each column
print(data.isnull().sum())
# Finding null values in a particular column
print("\nAge column null values: ", data['Age'].isnull().sum())
# Finding null values with boolean format
print(data.isnull())
print(data['Age'].isnull())

# For notnull()/ notna() is also another function to find the null
# values but it opposite to isnull() / isna()
print(data.notnull().sum())