import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.title("Weather World Dashboard")
st.write("Explore weather data scraped from cities around the world.")

with sqlite3.connect('weather.db') as conn:
    df = pd.read_sql_query("SELECT * FROM weather", conn)

st.sidebar.header("Filter Options")
selected_city = st.sidebar.selectbox("Select a City", df['city'])

filtered_df = df[df['city'] == selected_city]

col1, col2 = st.columns(2)
with col1:
    st.metric("Temperature (°F)", f"{filtered_df['Temperature_F'].values[0]}")
with col2:
    st.metric("Humidity (%)", f"{filtered_df['Humidity_Percent'].values[0]}")

st.subheader(f"Weather Description: {filtered_df['Description'].values[0]}")

st.subheader("Temperature by City")
fig1 = px.bar(df, x='city', y='Temperature_F', color='city', title="Temperature by City")
st.plotly_chart(fig1)

st.subheader("Humidity by City")
fig2 = px.bar(df, x='city', y='Humidity_Percent', color='city', title="Humidity by City")
st.plotly_chart(fig2)

st.subheader("Temperature vs Humidity")
fig3 = px.scatter(df, x='Temperature_F', y='Humidity_Percent', color='city', size='Humidity_Percent',
                   title="Temperature vs Humidity by City", hover_data=['Description'])
st.plotly_chart(fig3)