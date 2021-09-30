import missingno as msno
import pandas as pd

# Loading Data
data = pd.read_csv("data/titanic.csv")
# Matrix graph
msno.matrix(data)
msno.bar(data)
msno.heatmap(data)