# Proyek Analisis Data Penyewaan Sepeda 🚲

## Deskripsi
Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan dataset yang tersedia. Data yang digunakan mencakup informasi harian dan per jam mengenai jumlah penyewaan sepeda, kondisi cuaca, serta faktor lainnya yang dapat memengaruhi jumlah penyewaan.

## Teknik Analisis yang Digunakan
1. Pembersihan Data
Mengonversi kolom tanggal ke format datetime untuk mempermudah analisis berbasis waktu. Memfilter data berdasarkan rentang waktu yang ditentukan oleh pengguna.
2. Analisis Tren Penyewaan Sepeda
Menganalisis pola penyewaan sepeda berdasarkan hari dalam seminggu menggunakan visualisasi bar chart. Menggunakan seaborn untuk membuat grafik yang lebih informatif.
3. Perbandingan Hari Kerja vs Hari Libur
Membandingkan jumlah penyewaan sepeda pada hari kerja dan hari libur menggunakan pie chart. Menggunakan proporsi penyewaan sepeda untuk memperjelas distribusi antara kedua kategori.
4. Visualisasi Data
Menggunakan matplotlib dan seaborn untuk membuat grafik interaktif yang membantu memahami pola dalam data. Menambahkan warna khusus untuk membedakan kategori (misalnya, warna merah untuk hari kerja dan biru untuk hari libur).


## Setup Environment - Shell/Terminal

Menggunakan Conda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

Menggunakan Pipenv
mkdir ANALYSIS_DATA_PYTHON
cd ANALYSIS_DATA_PYTHON
pipenv install
pipenv shell
pip install -r requirements.txt

## Cara Menjalankan
1. Pastikan semua dependensi yang dibutuhkan telah terinstal (requirements.txt).
2. Jalankan aplikasi Streamlit dengan perintah:
streamlit run dashboard.py
3. Pilih rentang waktu yang diinginkan melalui sidebar untuk menyesuaikan analisis.





