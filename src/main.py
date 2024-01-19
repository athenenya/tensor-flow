import pandas as pd
from pathlib import Path

path = Path(__file__).parent / "./files/insurance.csv"
data = pd.read_csv(path, sep=";")
#C:\\Users\\Athene\\Documents\\PythonPrograms\\tensor-flow\\src\\files\\insurance.csv
print(data.head())
print(data.shape)
print(data.info())
print(data.isnull())
print(data.isnull().sum())
print(data.dtypes)
data['sex'] = data['sex'].astype('category')
data['region'] = data['region'].astype('category')
data['smoker'] = data['smoker'].astype('category')
print(data.dtypes)
print(data.describe().T)
#smoke_data = data.groupby("smoker").mean().round(2)
smoke_data = data.groupby("smoker").mean().round(2)
print(smoke_data)