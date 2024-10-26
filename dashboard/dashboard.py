import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
day_data = pd.read_csv('dashboard/day.csv')
day_data['dteday'] = pd.to_datetime(day_data['dteday'])  # Convert to datetime

# Title of the dashboard
st.title("Bike Usage Analysis Dashboard")

# Menampilkan dataset
st.write("Data Bike Sharing:")
st.write(day_data.head())

# Menambahkan sidebar untuk filter data
# Filter Rentang Tanggal
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input('Start date', day_data['dteday'].min())
end_date = st.sidebar.date_input('End date', day_data['dteday'].max())

# Filter berdasarkan tanggal
df_filter = day_data[(day_data['dteday'] >= pd.to_datetime(start_date)) & (day_data['dteday'] <= pd.to_datetime(end_date))]

# Filter Temperature / Suhu
temp_range = st.sidebar.slider('Temperature Range (Normalized)', 0.0, 1.0, (0.1, 0.9))
df_filter = df_filter[(df_filter['temp'] >= temp_range[0]) & (df_filter['temp'] <= temp_range[1])]

# Filter Humidity / Kelembaban
humidity_range = st.sidebar.slider('Humidity Range (Normalized)', 0.0, 1.0, (0.1, 0.9))
df_filter = df_filter[(df_filter['hum'] >= humidity_range[0]) & (df_filter['hum'] <= humidity_range[1])]

# Filter Windspeed / Kecepatan Angin
windspeed_range = st.sidebar.slider('Windspeed Range (Normalized)', 0.0, 1.0, (0.1, 0.9))
df_filter = df_filter[(df_filter['windspeed'] >= humidity_range[0]) & (df_filter['windspeed'] <= humidity_range[1])]

# Menampilkan hasil filter
st.subheader(f"Data dari {start_date} hingga {end_date}")
st.write(df_filter.head())

# Visualisasi Total Rentals vs Temperature dengan Filter
st.subheader('Total Rentals vs Temperature (Filter)')
fig, ax = plt.subplots()
sns.scatterplot(x=df_filter['temp'], y=df_filter['cnt'], ax=ax)
ax.set_title('Total Rentals vs Temperature')
ax.set_xlabel('Temperature (Normalized)')
ax.set_ylabel('Total Rentals')
st.pyplot(fig)

# Visualisasi Total Rentals vs Humidity dengan Filter
st.subheader('Total Rentals vs Humidity (Filter)')
fig, ax = plt.subplots()
sns.scatterplot(x=df_filter['hum'], y=df_filter['cnt'], ax=ax)
ax.set_title('Total Rentals vs Humidity')
ax.set_xlabel('Humidity (Normalized)')
ax.set_ylabel('Total Rentals')
st.pyplot(fig)

# Visualisasi Total Rentals vs Windspeed dengan Filter
st.subheader('Total Rentals vs Windspeed (Filter)')
fig, ax = plt.subplots()
sns.scatterplot(x=df_filter['windspeed'], y=df_filter['cnt'], ax=ax)
ax.set_title('Total Rentals vs windspeed')
ax.set_xlabel('Windspeed (Normalized)')
ax.set_ylabel('Total Rentals')
st.pyplot(fig)

# Visualisasi 1: Pengaruh cuaca terhadap penggunaan sepeda
st.subheader("Pengaruh Cuaca terhadap Penggunaan Sepeda")
fig1, ax1 = plt.subplots()
sns.boxplot(x='weathersit', y='cnt', data=df_filter, ax=ax1)
ax1.set_xlabel('Kondisi Cuaca (1: Cerah, 2: Mendung, 3: Hujan ringan)')
ax1.set_ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig1)

# Visualisasi 2: Pengaruh hari kerja vs hari libur terhadap penggunaan sepeda
st.subheader("Pengaruh Hari Kerja vs Hari Libur terhadap Penggunaan Sepeda")
fig2, ax2 = plt.subplots()
sns.boxplot(x='workingday', y='cnt', data=df_filter, ax=ax2)
ax2.set_xlabel('Hari Kerja (0: Libur, 1: Hari Kerja)')
ax2.set_ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig2)