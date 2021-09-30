import pandas as pd
import numpy as np

data = pd.read_csv("data/titanic.csv")
print(data)
print(data.isnull().sum())


def apply_mean():
    return data["Age"].mean()


def apply_median():
    return data["Age"].median()


def apply_mode():
    return data["Age"].mode()


data["Age"].replace(np.NaN, apply_mean(), inplace=True)
print(data.isnull().sum())