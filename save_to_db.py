# Task 6: Save cleaned weather data into a SQLite database
import sqlite3
import pandas as pd

df = pd.read_csv('clean_weather_data.csv')
print("Data loaded from CSV:")
print(df)

with sqlite3.connect('weather.db') as conn:
    df.to_sql('weather', conn, if_exists='replace', index=False)
    print("\nSaved to weather.db")

    check = pd.read_sql_query("SELECT * FROM weather", conn)
    print("\nVerifying data in database:")
    print(check)