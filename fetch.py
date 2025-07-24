import pandas as pd

# Load the CSV
df = pd.read_csv('/Users/ayush/Downloads/EnergyAnalytics/PUB_HourlyConsumptionByFSA_201801_v1.csv')

# Combine date + hour into a timestamp
df['DATETIME'] = pd.to_datetime(df['DATE'] + ' ' + df['HOUR'].astype(str) + ':00')

# Optional: Standardize customer type and price plan
df['CUSTOMER_TYPE'] = df['CUSTOMER_CLASS'].str.strip()
df['PRICE_PLAN'] = df['PRICE_PLAN'].str.strip()

# Convert consumption to float if it's not already
df['TOTAL_CONSUMPTION'] = pd.to_numeric(df['TOTAL_CONSUMPTION'], errors='coerce')