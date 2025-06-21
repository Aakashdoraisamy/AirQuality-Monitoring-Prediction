import pandas as pd

# Load dataset
data = pd.read_csv("archive/city_day.csv")  # Adjust path when deploying

# Date conversion and column renaming
data['Date'] = pd.to_datetime(data['Date'])
data.rename(columns={'AQI_Bucket': 'Air_quality'}, inplace=True)
