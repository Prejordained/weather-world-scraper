import pandas as pd
import re

df = pd.read_csv('raw_weather_data.csv')
print("BEFORE CLEANING:")
print(df)

df['Temperature_F'] = df['raw_data'].str.extract(r'\+(\d+)°F')
df['Humidity_Percent'] = df['raw_data'].str.extract(r'(\d+)%')
df['Description'] = df['raw_data'].str.extract(r':\s*(.+?)\s*\+')

clean_df = df[['city', 'Description', 'Temperature_F', 'Humidity_Percent']]

print("\nAFTER CLEANING:")
print(clean_df)

clean_df.to_csv('clean_weather_data.csv', index=False)
print("\nSaved to clean_weather_data.csv")