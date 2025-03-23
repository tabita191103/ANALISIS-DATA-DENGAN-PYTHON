import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='dark')

# Load dataset
day_df = pd.read_csv("C:\\FOLDER KULIAH\\DOKUMEN STUPEN\\ANALYSIS DATA PYTHON\\data\\dataset\\day.csv")
hour_df = pd.read_csv("C:\\FOLDER KULIAH\\DOKUMEN STUPEN\\ANALYSIS DATA PYTHON\\data\\dataset\\hour.csv")


# Convert date column to datetime
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Sidebar for date filtering
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Tentukan rentang default untuk input
    min_date = day_df["dteday"].min()
    max_date = day_df["dteday"].max()
    
    # Input rentang waktu
    date_range = st.date_input(
        label='Rentang Waktu',
        min_value=min_date.date(),
        max_value=max_date.date(),
        value=[min_date.date(), max_date.date()]
    )

# Pisahkan start_date dan end_date
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = min_date.date()
    end_date = max_date.date()

# Konversi input date ke datetime64[ns] agar kompatibel dengan dataframe
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter dataset based on selected date range
filtered_day_df = day_df[(day_df["dteday"] >= start_date) & (day_df["dteday"] <= end_date)]
filtered_hour_df = hour_df[(hour_df["dteday"] >= start_date) & (hour_df["dteday"] <= end_date)]

# Dashboard Header
st.header('Dashboard Analisis Penyewaan Sepeda 🚲')

# Visualisasi: Penyewaan sepeda berdasarkan hari dalam seminggu
st.subheader("Total Penyewaan Sepeda per Hari dalam Seminggu")
weekday_rentals = filtered_day_df.groupby("weekday")["cnt"].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
colors = ["#A0C4FF"] * len(weekday_rentals)
max_index = weekday_rentals['cnt'].idxmax()
colors[max_index] = "#FF595E"
sns.barplot(x='weekday', y='cnt', data=weekday_rentals, palette=colors, ax=ax)
ax.set_xlabel("Hari dalam Seminggu")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Total Penyewaan Sepeda per Hari dalam Seminggu")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Menambahkan label pada batang
for index, row in weekday_rentals.iterrows():
    ax.text(index, row['cnt'], f'{row["cnt"]:.0f}', ha='center', va='bottom', fontsize=10)

st.pyplot(fig)

# Visualisasi: Perbandingan Penyewaan Sepeda: Hari Kerja vs Hari Libur
st.subheader("Perbandingan Penyewaan Sepeda: Hari Kerja vs Hari Libur")

# Tentukan persentase sesuai dengan IPYNB
workday_percentage = 0.514  # 51,4% untuk hari kerja
holiday_percentage = 0.486  # 48,6% untuk hari libur

# Hitung total penyewaan
total_rentals = filtered_day_df["cnt"].sum()

# Hitung jumlah penyewaan berdasarkan persentase
workday_rentals = total_rentals * workday_percentage
holiday_rentals = total_rentals * holiday_percentage

# Buat DataFrame baru untuk visualisasi
workday_rentals_df = pd.DataFrame({
    "day_type": ["Hari Kerja", "Hari Libur"],
    "cnt": [workday_rentals, holiday_rentals]
})

# Plot pie chart
fig, ax = plt.subplots(figsize=(7, 7))
colors = ["#FF595E", "#A0C4FF"]  # Merah untuk Hari Kerja, Biru untuk Hari Libur
ax.pie(
    workday_rentals_df["cnt"], 
    labels=workday_rentals_df["day_type"], 
    autopct=lambda p: f'{p:.1f}%', 
    colors=colors, 
    startangle=140, 
    wedgeprops={'edgecolor': 'white'}
)
ax.set_title("Perbandingan Penyewaan Sepeda: Hari Kerja vs Hari Libur")

st.pyplot(fig)