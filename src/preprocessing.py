import pandas as pd

# Copying dataset
df1 = data.copy()

# Fill missing values using median
for col in ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3']:
    df1[col] = df1[col].fillna(df1[col].median())
