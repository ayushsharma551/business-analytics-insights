import pandas as pd

df = pd.read_csv('/Users/ayush/Documents/EnergyAnalytics/PUB_HourlyConsumptionByFSA_201801_v1.csv', skiprows=3)
print(df.head())

